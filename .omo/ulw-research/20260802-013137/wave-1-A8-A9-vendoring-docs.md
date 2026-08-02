# Wave 1 / A8 — Large-payload vendoring   +   A9 — Doc/template drift

## A8 sources
[S32] "Large files with Git: LFS and git-annex", LWN.net 774125.
[S33] Larson, "Managing Large Files in Git: LFS and Alternatives", grizzlypeaksoftware.com, 2026-02-13.
[S34] InSimo/lfs-experiments (GitHub) — 15-scenario benchmark on a real 22.5 GB / 20k-object repo.
[S35] "Benchmarking the Modern Development Experience across Versioning Tools: S3, DVC, Git LFS,
      and XetHub" (2024-07).
[S36] StackOverflow 79485088 "GIT LFS vs Annex For Thousands of Unchanging Binaries".

## A8 hard numbers
Free-tier LFS quotas [S33]: GitHub 1 GB storage + 1 GB/mo bandwidth ($5 per 50 GB pack; 2 GB
  per-FILE hard limit [S32]); GitLab 5 GB + 10 GB/mo; Bitbucket 1 GB + 1 GB; Azure DevOps ~250 GB
  and UNLIMITED bandwidth (the cost winner for LFS-heavy repos); self-hosted S3 ~$0.023/GB stored
  + ~$0.09/GB transfer.
LFS structural costs:
 - DOUBLES local disk: the payload is copied into .git/lfs/objects as well as the worktree [S32].
 - smudge/clean filters BUFFER WHOLE FILES IN MEMORY -> "prohibitive with files larger than
   available memory" [S32].
 - NO DEDUPLICATION across versions: each version is an independent blob. [S34] measured
   22.61 GB under LFS vs 6.98 GB for plain git on the same 500-version corpus (git's delta
   compression won 3.2x). Content-defined chunking (desync) got it to 4.02 GB = 5.6x better
   than LFS.
 - "Hotel California": practitioners report you can never really delete; size only grows [S36].
 - SILENT FAILURE MODE: if LFS is missing/misconfigured you check out a 130-140 byte POINTER FILE
   instead of the payload, producing "cryptic parsing errors" downstream. [S33] recommends
   explicit pointer/size validation in the build to fail fast.
Sizing rule of thumb [S33]: "Keep files under 5 MB in regular Git." LFS only where size justifies it.
git-annex [S32]: partial checkouts, location tracking (knows how many copies exist and where),
  `git annex fsck` verifies checksums and detects BITROT. Weaknesses: fragile on Windows, poorly
  supported by hosts (GitLab DROPPED it, calling it "a burden to support"), steep learning curve.
DVC [S33][S36]: content-addressed dedup, needs no special server (any S3/SSH you own), built for
  ML pipelines.
DIY S3 + committed manifest [S33]: explicitly endorsed — "Sometimes the simplest approach is the
  right one ... This avoids LFS bandwidth costs entirely." Recommended when you want full control
  and already have the storage.
[S32] closing advice, and the most important line for a 5.6 GB read-only corpus: "before adding
large files into Git, you might want to think about organizing your content correctly first."

## A9 sources
[S37] Keturakis, "We built a linter for documentation rot", Fiberplane blog, 2026-03-25.
      Tool: github.com/fiberplane/drift.
[S38] Vale (vale.sh) — offline prose linter, single Go binary, no runtime deps.
[S39] Antora docs: "Partials" and "Source Code Snippets and Examples" (partials/ + examples/ dirs,
      include:: with tag / tags / lines).
[S40] Zenzic (github.com/PythonWoods/zenzic) — engine-agnostic Markdown linter.

## A9 findings
SINGLE-SOURCING: Antora's model is the mature one — content lives in `partials/` and `examples/`,
  is pulled in by an `include::` directive, and can include only a named REGION via `tag=`/`tags=`
  or `lines=`. "When you change the content in a partial, those changes will disseminate to all of
  the pages where you embedded that partial." Antora also collects sources from MULTIPLE
  repositories into one site.
DRIFT DETECTION (the 2026 state of the art) [S37]: `drift` anchors a markdown spec to a code
  symbol via frontmatter `path#Symbol @commit`. It parses with tree-sitter and hashes a
  NORMALISED AST FINGERPRINT (node kinds + token text, no whitespace/position), so reformatting
  does not false-positive. `drift check` compares the bound symbol at the provenance commit against
  HEAD and exits 1 when stale. Supports TS, Python, Rust, Go, Zig, Java; falls back to raw content
  comparison elsewhere. Author's framing, which is the key point: "The real value isn't the tool,
  it's the constraint ... Agents are prolific code changers but terrible at knowing what else their
  change affects." Explicit honest limit: drift detects, it does not review; re-linking without
  updating prose still passes.
  Contrast drawn by [S37]: doctests and snippet-embedding tools keep CODE EXAMPLES in sync but do
  nothing for THE PROSE THAT DESCRIBES THEM. That is exactly the 16-runbook problem.
PROSE LINTING [S38]: Vale — offline, single Go binary, understands Markdown/AsciiDoc/rST/HTML,
  ships Microsoft and Google style packages, drops into CI or a pre-commit hook.
EXECUTABLE DOCS [S40]: `zenzic check snippets` validates Python/YAML/JSON/TOML fenced blocks parse;
  `check links` finds broken internal links and dead anchors; `check orphans` finds files absent
  from nav; `zenzic score` gives a deterministic 0-100 and `zenzic diff` does regression detection
  against a saved baseline. 100% subprocess-free static analysis.

## EXPAND
- DEAD END: DITA. Nothing in the 2024-2026 material recommends it for a code-adjacent repo; the
  live options are Antora partials (AsciiDoc), MkDocs/Sphinx includes, or generation from data.
