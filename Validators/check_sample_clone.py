#!/usr/bin/env python3
"""
Sample-clone fingerprint. V5 calls this check non-waivable.

Fingerprints a candidate prompt against every sample in its universe's comparison corpus
on seven elements:

    1. Core scenario
    2. Persona paired with that scenario
    3. Named entities
    4. Ask set and deliverables
    5. Service and write mix
    6. Workflow shape
    7. Distinctive phrasing

WHAT IS ACTUALLY COMPUTED, AND WHAT IS NOT
------------------------------------------
Three of the seven are mechanical. Two are partial: a mechanical sub-signal exists but it
cannot settle the element. Two are irreducibly semantic and are NOT scored here - faking
them with a keyword proxy and reporting the result next to a real measurement would make
the whole fingerprint untrustworthy, so they are emitted as a structured adjudication
prompt naming exactly what a human or council must compare.

    E1 Core scenario        SURFACED    semantic
    E2 Persona + pairing    PARTIAL     persona identity is exact; the PAIRING is semantic
    E3 Named entities       MECHANICAL  rarity-weighted entity overlap
    E4 Ask set/deliverables PARTIAL     deliverable + write-verb sets; the ASK SEMANTICS are not
    E5 Service/write mix    MECHANICAL  registry-derived service inference + write-verb set
    E6 Workflow shape       SURFACED    semantic
    E7 Distinctive phrasing MECHANICAL  rare shingles, sentence reuse, opening-line reuse

E5's service inference is keyword-based over a registry-derived map. That is a documented
approximation, not comprehension. It is tolerable precisely because a service-mix match can
never on its own drive a failure (see the "explicitly fine" list below).

HARD-FAIL CONDITIONS
--------------------
    HF1  a full sentence, or the opening line, reused or lightly reworded   [mechanical]
    HF2  four or more of the seven match a single sample                    [mechanical floor]
    HF3  same scenario AND the same named entities                          [needs E1]
    HF4  same persona, same scenario and the same asks lifted together      [needs E1]

HF1 and HF2 are decided here. HF3 and HF4 each depend on E1, which is semantic, so this
check pre-fills their mechanical half and escalates the rest rather than guessing.

EXPLICITLY FINE - these must NOT flag
-------------------------------------
    - same persona on a different scenario
    - same services or same task category
    - same investigate-then-act shape with different content
    - ordinary universe vocabulary (channel names, tool nouns, the universe date)

The fourth is the false-positive trap, and it is the reason this file spends more code on
neutralising shared vocabulary than on measuring overlap. Two independent mechanisms:

    (a) REGISTRY STOPLIST. Services, Slack channels, NPCs, personas, the domain, the email
        domain and the universe date are ordinary vocabulary BY CONSTRUCTION, so they are
        read out of the registry rather than hand-listed.
    (b) CORPUS DOCUMENT FREQUENCY. Anything appearing in a large fraction of the corpus is
        cast or setting, not a distinctive signal, and is down-weighted to zero. This is
        what stops a shared cast (every HarmonyGames prompt mentions Arthur or Leonard)
        from reading as a copied entity set.

Usage:
    python Validators/check_sample_clone.py <path_to_task_dir>
    python Validators/check_sample_clone.py <path_to_task_dir> --explain <sample_dir>
    python Validators/check_sample_clone.py --matrix <universe>
    python Validators/check_sample_clone.py --matrix <universe> --no-deprecated

Exit codes:
    0  clear
    1  HARD FAIL (HF1 or HF2)
    3  ADJUDICATION REQUIRED (a semantic element must be settled before this can clear)
    2  usage error
"""

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
from universes import UNIVERSES, get_universe_constants  # noqa: E402
from calc_similarity import corpus_globs, read_optional, resolve_task_dir, resolve_universe  # noqa: E402

# ---------------------------------------------------------------------------
# Tunables. Every one of these was calibrated against the real corpus and the
# calibration is reproducible with --matrix; none of them is a guess.
# ---------------------------------------------------------------------------

# A term is ordinary vocabulary when this fraction of the OTHER samples - the corpus
# minus the two documents being compared - also uses it.
#
# Excluding the pair is not a refinement, it is the whole point. Counting document
# frequency over the full corpus made the check structurally blind to the thing it
# exists to catch: on a 7-sample corpus the cut landed at 2, so any term shared by
# exactly two documents was discarded as "setting" - and a copy plus its source is
# exactly two documents. A verbatim clone neutralised itself and scored zero. The
# corpus-vs-corpus matrix looked immaculate for the same reason.
DF_VOCAB_FRACTION = 0.34
VOCAB_MIN_OTHER_DOCS = 2

# Shingle width for "distinctive phrasing". Five words is long enough that an
# incidental collocation ("one row per pull request") does not register, and short
# enough to survive light rewording of the surrounding sentence.
SHINGLE_N = 5

# A sentence needs this many content words before reuse of it means anything. Short
# sentences ("Thanks.", "Post it in the channel.") collide constantly and innocently.
SENTENCE_MIN_CONTENT = 8

# Token-Jaccard at which two sentences are "lightly reworded" rather than merely similar.
SENTENCE_REWORD_J = 0.80
OPENING_REWORD_J = 0.60

# Per-element match thresholds.
E3_ENTITY_MATCH = 0.34
E4_ASK_MATCH = 0.60
E5_SERVICE_MATCH = 0.70
E7_PHRASING_MATCH = 0.10

STOP_WORDS = {
    "the", "a", "an", "and", "or", "but", "if", "then", "than", "that", "this", "these",
    "those", "is", "are", "was", "were", "be", "been", "being", "am", "do", "does", "did",
    "have", "has", "had", "i", "you", "he", "she", "it", "we", "they", "me", "him", "her",
    "us", "them", "my", "your", "his", "its", "our", "their", "what", "which", "who",
    "whom", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more",
    "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so",
    "too", "very", "can", "will", "just", "should", "now", "of", "to", "in", "for", "on",
    "with", "at", "by", "from", "up", "out", "off", "over", "under", "again", "there",
    "here", "as", "about", "into", "through", "during", "before", "after", "above",
    "below", "between", "because", "while", "would", "could", "want", "get", "got", "go",
    "going", "know", "think", "like", "make", "made", "take", "put", "let", "still",
    "also", "back", "one", "two", "s", "t", "don", "didn", "isn", "wasn", "im", "ive",
}

# Element 5. Keys are registry service names; values are the prose a persona would
# actually use. Only services the universe declares are consulted, so this map is
# filtered by the registry rather than assumed.
SERVICE_WORDS = {
    "slack": {"channel", "slack", "pinned", "pin", "thread", "dm", "post", "posted"},
    "github": {"pull", "request", "prs", "pr", "repo", "repository", "commit", "commits",
               "merge", "merged", "branch", "review", "reviewer", "diff", "code"},
    "gsheets": {"spreadsheet", "sheet", "tab", "register", "row", "rows", "column"},
    "gdocs": {"doc", "docs", "document", "writeup", "write-up", "memo"},
    "gdrive": {"drive", "folder", "file", "upload", "uploaded"},
    "gcal": {"calendar", "invite", "meeting", "huddle", "slot", "schedule"},
    "gmail": {"email", "emailed", "mail", "inbox", "mailbox", "reply"},
    "gslides": {"slide", "slides", "deck", "presentation"},
    "linear": {"ticket", "tickets", "issue", "issues", "backlog", "tracker", "sprint"},
    "trello": {"board", "card", "cards", "list"},
    "contacts": {"contact", "contacts", "roster", "directory"},
    "email": {"email", "emailed", "mail", "inbox", "mailbox", "reply"},
    "calendar": {"calendar", "invite", "meeting", "slot", "schedule"},
    "airtable": {"airtable", "base", "record", "records", "table"},
    "quickbooks": {"quickbooks", "invoice", "bill", "ledger", "payment"},
    "crm": {"crm", "deal", "engagement", "pipeline"},
    "hubspot": {"hubspot", "crm", "deal", "contact"},
    "oracle_gl": {"journal", "entry", "gl", "ledger", "account", "posting"},
    "sap_subledger": {"subledger", "sap", "ap", "invoice"},
    "blackline": {"reconciliation", "recon", "exception", "blackline"},
    "records_vault": {"vault", "retention", "document", "classification"},
    "mortgage_los": {"loan", "borrower", "disclosure", "underwriting", "closing"},
    "stripe": {"charge", "payment", "stripe"},
    "filesystem": {"file", "folder", "pdf"},
    "gcalendar": {"calendar", "invite", "meeting", "slot", "schedule"},
    "public": {"public"},
}

WRITE_VERBS = {
    "post", "posted", "send", "sent", "create", "created", "add", "added", "update",
    "updated", "comment", "commented", "file", "filed", "open", "opened", "close",
    "closed", "reopen", "flip", "mark", "marked", "schedule", "scheduled", "share",
    "shared", "upload", "uploaded", "draft", "log", "record", "assign", "assigned",
    "write", "reflect", "track", "tracked", "note",
}

DELIVERABLE_NOUNS = {
    "spreadsheet", "register", "memo", "doc", "document", "summary", "rundown", "readout",
    "report", "pack", "ticket", "comment", "message", "post", "email", "tab", "link",
    "count", "note", "brief", "list", "sheet", "writeup", "recap", "status",
}


# ---------------------------------------------------------------------------
# Text primitives
# ---------------------------------------------------------------------------

def norm_tokens(text):
    text = text.lower().replace("\u2019", "'")
    text = re.sub(r"[^\w\s'-]", " ", text)
    return [t.strip("'-") for t in text.split() if t.strip("'-")]


def content_tokens(text):
    return [t for t in norm_tokens(text) if t not in STOP_WORDS and len(t) > 2]


def sentences(text):
    parts = re.split(r"(?<=[.!?])\s+|\n+", text)
    return [p.strip() for p in parts if p.strip()]


def shingles(tokens, n=SHINGLE_N):
    return {" ".join(tokens[i:i + n]) for i in range(len(tokens) - n + 1)}


def jaccard(a, b):
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def entities(text):
    """Capitalised runs, hashtag channels, repo paths, ALLCAPS flags, hyphenated slugs.

    Sentence-initial capitals are the obvious false-entity source. They are not filtered
    here: the document-frequency pass removes them far more reliably than a hand-built
    English word list would, because a sentence-initial "Check" or "Once" recurs across
    the corpus and so is discarded as setting.
    """
    found = set()
    for m in re.finditer(r"\b[A-Z][a-zA-Z0-9]*(?:[ -][A-Z][a-zA-Z0-9]*)*\b", text):
        found.add(m.group(0).strip())
    found |= set(re.findall(r"#[a-z0-9][a-z0-9._-]+", text))
    found |= set(re.findall(r"\b[a-zA-Z0-9_.-]+/[a-zA-Z0-9_.-]+\b", text))
    found |= set(re.findall(r"\b[A-Z]{3,}(?:_[A-Z0-9]+)*\b", text))
    return {e for e in found if len(e) > 2}


# ---------------------------------------------------------------------------
# Corpus
# ---------------------------------------------------------------------------

def injected_text(task_dir):
    """The injected thread. The memo asks for it because copied content often lives there.

    Empty for every vendored HarmonyGames sample as of the V5 drop: all seven changelogs
    are `[]` and no 9_Universe_inject.sql is vendored, so this contributes nothing to the
    corpus today. It is read anyway because a live task under construction does carry one.
    """
    chunks = []
    sql = task_dir / "9_Universe_inject.sql"
    if sql.is_file():
        try:
            body = sql.read_text(encoding="utf-8", errors="replace")
        except OSError:
            body = ""
        # Comment-only template headers carry no injected content.
        body = "\n".join(ln for ln in body.splitlines() if not ln.strip().startswith("--"))
        if body.strip():
            chunks.append(body)
    log = task_dir / "4_Changelog.json"
    if log.is_file():
        try:
            data = json.loads(log.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            data = None
        chunks.extend(_strings_in(data))
    return "\n".join(chunks)


def _strings_in(node, depth=0):
    """Every human-readable string in a nested changelog, regardless of its schema."""
    if depth > 8:
        return []
    if isinstance(node, str):
        return [node] if len(node) > 12 else []
    if isinstance(node, dict):
        out = []
        for v in node.values():
            out.extend(_strings_in(v, depth + 1))
        return out
    if isinstance(node, list):
        out = []
        for v in node:
            out.extend(_strings_in(v, depth + 1))
        return out
    return []


def load_doc(prompt_path):
    task_dir = prompt_path.parent
    try:
        prompt = prompt_path.read_text(encoding="utf-8").strip()
    except (OSError, UnicodeDecodeError):
        return None
    if not prompt:
        return None
    try:
        rel = str(prompt_path.relative_to(ROOT))
        dir_rel = str(task_dir.relative_to(ROOT))
    except ValueError:
        rel, dir_rel = str(prompt_path), str(task_dir)
    inj = injected_text(task_dir)
    return {
        "path": rel,
        "task_dir": dir_rel,
        "name": task_dir.name,
        "origin": "qc_sample" if rel.startswith("QC_Tasks") else "project_task",
        "deprecated": "_DEPRECATED" in task_dir.name,
        "prompt": prompt,
        "injected": inj,
        "text": prompt + ("\n" + inj if inj else ""),
        "persona": read_optional(task_dir / "2_Persona.txt"),
        "business_function": read_optional(task_dir / "1_Business_Function.txt"),
    }


def load_corpus(universe, self_path=None, qc_only=True, include_deprecated=True):
    docs = []
    for base, pattern in corpus_globs(universe):
        if not base.is_dir():
            continue
        for p in sorted(base.glob(pattern)):
            if self_path is not None and p.resolve() == Path(self_path).resolve():
                continue
            d = load_doc(p)
            if d is None:
                continue
            if qc_only and d["origin"] != "qc_sample":
                continue
            if d["deprecated"] and not include_deprecated:
                continue
            docs.append(d)
    return docs


# ---------------------------------------------------------------------------
# Vocabulary neutralisation
# ---------------------------------------------------------------------------

def registry_stoplist(universe):
    """Ordinary universe vocabulary, read out of the registry rather than hand-listed."""
    try:
        c = get_universe_constants(universe)
    except Exception:
        return set()
    out = set()

    def add(v):
        if isinstance(v, str):
            for t in norm_tokens(v):
                out.add(t)
        elif isinstance(v, dict):
            for k, sub in v.items():
                add(k)
                add(sub)
        elif isinstance(v, (list, set, tuple)):
            for sub in v:
                add(sub)

    for key in ("services", "slack_channels", "npcs", "personas", "domain", "name",
                "persona_email_domain", "today", "business_functions",
                "acl_scoped_services", "acl_unscoped_services", "retired_services"):
        if key in c:
            add(c[key])
    out |= {w for words in SERVICE_WORDS.values() for w in words}
    return out


def build_context(universe, docs):
    """Document frequency over the corpus, plus the registry stoplist."""
    n = max(len(docs), 1)
    tok_df, ent_df, sh_df = {}, {}, {}
    for d in docs:
        toks = content_tokens(d["text"])
        for t in set(toks):
            tok_df[t] = tok_df.get(t, 0) + 1
        for e in entities(d["text"]):
            ent_df[e] = ent_df.get(e, 0) + 1
        for s in shingles(norm_tokens(d["text"])):
            sh_df[s] = sh_df.get(s, 0) + 1
    cut = max(VOCAB_MIN_OTHER_DOCS, -(-int(DF_VOCAB_FRACTION * max(n - 2, 1) * 100) // 100))
    return {
        "universe": universe,
        "n_docs": n,
        "stoplist": registry_stoplist(universe),
        "tok_df": tok_df, "ent_df": ent_df, "sh_df": sh_df,
        "df_cut": cut,
    }


def _pair_vocab(df, a_set, b_set, ctx):
    """Terms that are setting rather than signal, for THIS pair.

    effective_df is the number of samples OTHER than the two being compared that also
    carry the term. A term only the pair shares has effective_df 0 and survives, which
    is what makes a clone detectable at all.
    """
    cut = ctx["df_cut"]
    out = set()
    for term in (a_set | b_set):
        eff = df.get(term, 0) - (1 if term in a_set else 0) - (1 if term in b_set else 0)
        if eff >= cut:
            out.add(term)
    return out


def _registry_filtered_entities(text, ctx):
    out = set()
    for e in entities(text):
        toks = norm_tokens(e)
        if not toks or all(t in ctx["stoplist"] for t in toks):
            continue
        out.add(e)
    return out


def distinctive_entities(text, ctx, other_text=None):
    """Entities minus registry vocabulary minus what the OTHER samples share.

    `other_text` is the document being compared against. It is required for the pair
    exclusion; passing None falls back to a corpus-wide cut and is used only for the
    single-document diagnostics printed by --matrix.
    """
    ea = _registry_filtered_entities(text, ctx)
    if other_text is None:
        return {e for e in ea if ctx["ent_df"].get(e, 0) < ctx["df_cut"]}
    eb = _registry_filtered_entities(other_text, ctx)
    return ea - _pair_vocab(ctx["ent_df"], ea, eb, ctx)


def distinctive_shingles(text, ctx, other_text=None):
    sa = shingles(norm_tokens(text))
    if other_text is None:
        return {s for s in sa if ctx["sh_df"].get(s, 0) < ctx["df_cut"]}
    sb = shingles(norm_tokens(other_text))
    return sa - _pair_vocab(ctx["sh_df"], sa, sb, ctx)


# ---------------------------------------------------------------------------
# The seven elements
# ---------------------------------------------------------------------------

def e2_persona(a, b):
    pa, pb = a.get("persona"), b.get("persona")
    if not pa or not pb:
        return {"status": "PARTIAL", "match": None, "score": None,
                "evidence": "persona file absent on one side"}
    na = _persona_name(pa)
    nb = _persona_name(pb)
    same = na is not None and na == nb
    return {"status": "PARTIAL", "match": same, "score": 1.0 if same else 0.0,
            "evidence": f"persona {na!r} vs {nb!r}"}


def _persona_name(block):
    m = re.search(r"Name:\s*(.+)", block)
    return m.group(1).strip().lower() if m else block.strip().lower() or None


def e3_entities(a, b, ctx):
    ea = distinctive_entities(a["text"], ctx, b["text"])
    eb = distinctive_entities(b["text"], ctx, a["text"])
    j = jaccard(ea, eb)
    shared = sorted(ea & eb)
    return {"status": "MECHANICAL", "match": j >= E3_ENTITY_MATCH, "score": round(j, 3),
            "evidence": f"{len(shared)} distinctive entities shared: {shared[:10]}"}


def _service_mix(text, universe):
    try:
        declared = set(get_universe_constants(universe).get("services") or [])
    except Exception:
        declared = set()
    toks = set(norm_tokens(text))
    hits = set()
    for svc, words in SERVICE_WORDS.items():
        if declared and svc not in declared:
            continue
        if toks & words:
            hits.add(svc)
    return hits


def e5_services(a, b, ctx):
    sa = _service_mix(a["text"], ctx["universe"])
    sb = _service_mix(b["text"], ctx["universe"])
    wa = set(norm_tokens(a["text"])) & WRITE_VERBS
    wb = set(norm_tokens(b["text"])) & WRITE_VERBS
    j = (jaccard(sa, sb) + jaccard(wa, wb)) / 2
    return {"status": "MECHANICAL", "match": j >= E5_SERVICE_MATCH, "score": round(j, 3),
            "evidence": f"services {sorted(sa)} vs {sorted(sb)}; "
                        f"write verbs shared {sorted(wa & wb)[:8]}",
            "never_fails_alone": True}


def e4_asks(a, b, ctx):
    da = set(norm_tokens(a["text"])) & DELIVERABLE_NOUNS
    db = set(norm_tokens(b["text"])) & DELIVERABLE_NOUNS
    j = jaccard(da, db)
    return {"status": "PARTIAL", "match": j >= E4_ASK_MATCH, "score": round(j, 3),
            "evidence": f"deliverables {sorted(da)} vs {sorted(db)}; "
                        f"shared {sorted(da & db)}"}


def e7_phrasing(a, b, ctx):
    sa = distinctive_shingles(a["text"], ctx, b["text"])
    sb = distinctive_shingles(b["text"], ctx, a["text"])
    j = jaccard(sa, sb)
    shared = sorted(sa & sb)

    reused, reworded = [], []
    a_sents = [(s, set(content_tokens(s))) for s in sentences(a["prompt"])]
    b_sents = [(s, set(content_tokens(s))) for s in sentences(b["prompt"])]
    for s1, t1 in a_sents:
        if len(t1) < SENTENCE_MIN_CONTENT:
            continue
        for s2, t2 in b_sents:
            if len(t2) < SENTENCE_MIN_CONTENT:
                continue
            sim = jaccard(t1, t2)
            if sim >= 0.999:
                reused.append(s1)
            elif sim >= SENTENCE_REWORD_J:
                reworded.append((round(sim, 2), s1, s2))

    opening = 0.0
    if a_sents and b_sents:
        opening = jaccard(a_sents[0][1], b_sents[0][1])

    return {"status": "MECHANICAL", "match": j >= E7_PHRASING_MATCH, "score": round(j, 3),
            "evidence": f"{len(shared)} distinctive {SHINGLE_N}-grams shared: {shared[:5]}",
            "verbatim_sentences": reused,
            "reworded_sentences": reworded,
            "opening_similarity": round(opening, 3)}


def fingerprint(a, b, ctx):
    els = {
        "E1_core_scenario": {"status": "SURFACED", "match": None, "score": None,
                             "evidence": "semantic - not computed here"},
        "E2_persona_pairing": e2_persona(a, b),
        "E3_named_entities": e3_entities(a, b, ctx),
        "E4_asks_deliverables": e4_asks(a, b, ctx),
        "E5_service_write_mix": e5_services(a, b, ctx),
        "E6_workflow_shape": {"status": "SURFACED", "match": None, "score": None,
                              "evidence": "semantic - not computed here"},
        "E7_distinctive_phrasing": e7_phrasing(a, b, ctx),
    }

    confirmed = [k for k, v in els.items() if v["match"] is True]
    undecided = [k for k, v in els.items() if v["match"] is None]

    ph = els["E7_distinctive_phrasing"]
    hard = []
    if ph["verbatim_sentences"]:
        hard.append(f"HF1 verbatim sentence reused: {ph['verbatim_sentences'][0][:90]!r}")
    if ph["reworded_sentences"]:
        sim, s1, _ = ph["reworded_sentences"][0]
        hard.append(f"HF1 sentence lightly reworded (token overlap {sim}): {s1[:90]!r}")
    if ph["opening_similarity"] >= OPENING_REWORD_J:
        hard.append(f"HF1 opening line reused (token overlap {ph['opening_similarity']})")
    if len(confirmed) >= 4:
        hard.append(f"HF2 {len(confirmed)} of 7 elements match: {', '.join(confirmed)}")

    adjud = []
    if els["E3_named_entities"]["match"]:
        adjud.append(
            "HF3 needs E1. Named entities already MATCH. Compare the core scenario: is this "
            "the same underlying situation as the sample, or a different situation that "
            "reuses the same cast? Same scenario + these entities = hard fail.")
    if els["E2_persona_pairing"]["match"] and els["E4_asks_deliverables"]["match"]:
        adjud.append(
            "HF4 needs E1. Persona MATCHES and the ask/deliverable set MATCHES. Compare the "
            "core scenario. Same persona + same scenario + these asks lifted together = "
            "hard fail. Same persona on a DIFFERENT scenario is explicitly fine.")
    if len(confirmed) == 3 and undecided:
        adjud.append(
            f"HF2 is one element away: {len(confirmed)} of 7 confirmed mechanically "
            f"({', '.join(confirmed)}). If a reviewer judges any of "
            f"{', '.join(undecided)} to match, this reaches the four-of-seven bar.")

    verdict = "HARD_FAIL" if hard else ("ADJUDICATION_REQUIRED" if adjud else "CLEAR")
    return {
        "sample": b["path"], "sample_name": b["name"], "deprecated": b["deprecated"],
        "elements": els, "confirmed": confirmed, "confirmed_count": len(confirmed),
        "hard_fail_reasons": hard, "adjudication": adjud, "verdict": verdict,
    }


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------

def print_pair(res, verbose=False):
    print(f"--- vs {res['sample_name']}"
          f"{'  [DEPRECATED]' if res['deprecated'] else ''}")
    for k, v in res["elements"].items():
        mark = {True: "MATCH ", False: "differ", None: "  --  "}[v["match"]]
        score = "    " if v["score"] is None else f"{v['score']:.2f}"
        print(f"    {k:<24} {v['status']:<11} {mark} {score}   {v['evidence'][:88]}")
    print(f"    => {res['verdict']}  ({res['confirmed_count']}/7 mechanically confirmed)")
    for r in res["hard_fail_reasons"]:
        print(f"    [HARD FAIL] {r}")
    for r in res["adjudication"]:
        print(f"    [ADJUDICATE] {r}")


def run_matrix(universe, include_deprecated):
    docs = load_corpus(universe, qc_only=True, include_deprecated=include_deprecated)
    if len(docs) < 2:
        print(f"ERROR: corpus for {universe} has {len(docs)} sample(s)", file=sys.stderr)
        return 2
    ctx = build_context(universe, docs)
    print(f"=== sample-clone matrix: {universe} ===")
    print(f"corpus: {len(docs)} samples "
          f"({sum(1 for d in docs if d['deprecated'])} deprecated) · "
          f"vocab cut={ctx['df_cut']} other docs of {ctx['n_docs']} · "
          f"stoplist={len(ctx['stoplist'])} terms")
    print(f"injected thread present in "
          f"{sum(1 for d in docs if d['injected'])} of {len(docs)} samples")
    print()
    names = [d["name"][:26] for d in docs]
    print("confirmed-element counts (row = candidate, col = sample; 7 = self)")
    print(f"{'':<28}" + "".join(f"{i:>4}" for i in range(len(docs))))
    worst = 0
    for i, a in enumerate(docs):
        row = []
        for j, b in enumerate(docs):
            if i == j:
                row.append(7)
                continue
            r = fingerprint(a, b, ctx)
            row.append(r["confirmed_count"])
            worst = max(worst, r["confirmed_count"])
        print(f"{i:>2} {names[i]:<25}" + "".join(f"{v:>4}" for v in row))
    print()
    print("verdicts (off-diagonal only)")
    for i, a in enumerate(docs):
        for j, b in enumerate(docs):
            if i == j:
                continue
            r = fingerprint(a, b, ctx)
            if r["verdict"] != "CLEAR":
                print(f"  [{r['verdict']}] {names[i]} -> {names[j]}")
                for x in r["hard_fail_reasons"] + r["adjudication"]:
                    print(f"        {x}")
    print()
    print("self-comparison control (a sample against itself must max out)")
    ctl = fingerprint(docs[0], docs[0], ctx)
    print(f"  {names[0]} vs itself: {ctl['confirmed_count']}/7 confirmed, "
          f"verdict {ctl['verdict']}")
    print(f"\nmax off-diagonal confirmed-element count: {worst} (hard-fail bar is 4)")
    return 0


def main():
    ap = argparse.ArgumentParser(
        description="Fingerprint a prompt against its universe's QC samples on the "
                    "seven sample-clone elements.")
    ap.add_argument("task_dir", nargs="?", help="task directory containing 5_Prompt.txt")
    ap.add_argument("--explain", dest="explain_path", default=None,
                    help="print the full element breakdown against ONE sample dir")
    ap.add_argument("--matrix", dest="matrix_universe", default=None,
                    help="corpus-vs-corpus matrix for a universe (calibration mode)")
    ap.add_argument("--no-deprecated", action="store_true",
                    help="exclude _DEPRECATED samples from the comparison corpus")
    ap.add_argument("--include-project-tasks", action="store_true",
                    help="also compare against live task prompts, not just QC samples")
    args = ap.parse_args()

    if args.matrix_universe:
        if args.matrix_universe not in UNIVERSES:
            print(f"ERROR: unknown universe {args.matrix_universe!r}", file=sys.stderr)
            sys.exit(2)
        sys.exit(run_matrix(args.matrix_universe, not args.no_deprecated))

    if not args.task_dir:
        ap.print_usage(sys.stderr)
        print("ERROR: task_dir is required unless --matrix is given", file=sys.stderr)
        sys.exit(2)

    task_dir = resolve_task_dir(args.task_dir)
    if not task_dir.is_dir():
        print(f"ERROR: {args.task_dir} not a directory", file=sys.stderr)
        sys.exit(2)
    self_path = task_dir / "5_Prompt.txt"
    if not self_path.is_file():
        print(f"ERROR: {self_path} not found", file=sys.stderr)
        sys.exit(2)
    cand = load_doc(self_path)
    if cand is None:
        print(f"ERROR: {self_path} is empty", file=sys.stderr)
        sys.exit(2)

    universe = resolve_universe(task_dir)
    if args.explain_path:
        ex = resolve_task_dir(args.explain_path)
        target = load_doc(ex / "5_Prompt.txt") or load_doc(ex / "Prompt.txt")
        if target is None:
            print(f"ERROR: no readable prompt under {ex}", file=sys.stderr)
            sys.exit(2)
        docs = load_corpus(universe, self_path=self_path, qc_only=True)
        ctx = build_context(universe, docs + [cand])
        print(f"=== sample-clone EXPLAIN: {task_dir.name} vs {target['name']} ===")
        print_pair(fingerprint(cand, target, ctx), verbose=True)
        sys.exit(0)

    docs = load_corpus(universe, self_path=self_path,
                       qc_only=not args.include_project_tasks,
                       include_deprecated=not args.no_deprecated)
    ctx = build_context(universe, docs + [cand])
    results = [fingerprint(cand, d, ctx) for d in docs]
    results.sort(key=lambda r: (-r["confirmed_count"], r["sample_name"]))

    hard = [r for r in results if r["verdict"] == "HARD_FAIL"]
    adj = [r for r in results if r["verdict"] == "ADJUDICATION_REQUIRED"]

    print(f"=== sample-clone fingerprint: {task_dir.name} ===")
    print(f"universe:  {universe}")
    print(f"corpus:    {len(docs)} sample(s) from "
          f"{get_universe_constants(universe)['qc_reference_path']}")
    print(f"mechanical: E3 named entities, E5 service/write mix, E7 distinctive phrasing")
    print(f"partial:    E2 persona identity, E4 deliverable set")
    print(f"surfaced:   E1 core scenario, E6 workflow shape (semantic, not computed)")
    print()
    for r in results:
        print_pair(r)
    print()

    out = {
        "task": task_dir.name, "universe": universe, "corpus_size": len(docs),
        "mechanical_elements": ["E3_named_entities", "E5_service_write_mix",
                                "E7_distinctive_phrasing"],
        "partial_elements": ["E2_persona_pairing", "E4_asks_deliverables"],
        "surfaced_elements": ["E1_core_scenario", "E6_workflow_shape"],
        "results": results,
        "verdict": "HARD_FAIL" if hard else ("ADJUDICATION_REQUIRED" if adj else "CLEAR"),
    }
    out_path = task_dir / "_aux" / "Sample_Clone_Report.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(f"Written: {out_path}")

    if hard:
        print(f"\n[FAIL] {len(hard)} sample(s) hard-fail the clone check.")
        sys.exit(1)
    if adj:
        print(f"\n[ADJUDICATE] {len(adj)} sample(s) need a semantic call before this clears.")
        print("             E1/E6 are not computed here by design. Settle them, then re-run.")
        sys.exit(3)
    print("\n[OK] no sample reaches the clone bar.")
    sys.exit(0)


if __name__ == "__main__":
    main()
