#!/usr/bin/env python3
"""
Generate a paste-into-browser-console script that fills a platform rubric form
from a local 7_Rubrics.json. Auto-discovers the form layout -- no hand-written
selectors needed in the common case.

    python3 make_fill_script.py Tasks/<TASK_DIR>/7_Rubrics.json > fill.js

Then: open the rubric page, DevTools console, paste, Enter, follow the prompts.
"""
import json
import sys
from pathlib import Path

src = Path(sys.argv[1] if len(sys.argv) > 1 else "7_Rubrics.json")
rubrics = json.loads(src.read_text(encoding="utf-8"))
payload = json.dumps(rubrics, ensure_ascii=False, indent=2)

TEMPLATE = r"""
// ==============================================================
// RUBRIC FILLER -- @@N@@ criteria from @@SRC@@
//   1. PROBE()                 see what the page looks like
//   2. FILL({dryRun:true})     see what would be written where
//   3. FILL()                  write it
//   4. VERIFY()                read it back and diff
// Nothing is typed into the page until you call FILL() without dryRun.
// ==============================================================

const RUBRICS = @@PAYLOAD@@;

// ---------- React-safe writing --------------------------------
// `el.value = x` does not work on React controlled inputs: React caches the
// last value on the node, sees no change, and never fires onChange -- the field
// looks filled but submits empty. Go through the native prototype setter, then
// dispatch a bubbling input event so React's synthetic handler runs.
function setNativeValue(el, value) {
  if (el.isContentEditable) {
    el.focus();
    document.execCommand('selectAll', false, null);
    document.execCommand('insertText', false, value);   // most reliable for rich editors
    el.dispatchEvent(new Event('input', { bubbles: true }));
    return;
  }
  const proto = el instanceof HTMLTextAreaElement ? HTMLTextAreaElement.prototype
              : el instanceof HTMLSelectElement   ? HTMLSelectElement.prototype
              : HTMLInputElement.prototype;
  const setter = Object.getOwnPropertyDescriptor(proto, 'value').set;
  el.focus();
  setter.call(el, value);
  el.dispatchEvent(new Event('input',  { bubbles: true }));
  el.dispatchEvent(new Event('change', { bubbles: true }));
  el.blur();
}

const sleep = ms => new Promise(r => setTimeout(r, ms));
const visible = el => !!(el.offsetParent || el.getClientRects().length);

// ---------- field discovery -----------------------------------
function allFields() {
  return [...document.querySelectorAll(
    'input:not([type=hidden]):not([type=checkbox]):not([type=radio]):not([type=submit]):not([type=button]), ' +
    'textarea, select, [contenteditable="true"]'
  )].filter(visible).filter(el => !el.disabled && !el.readOnly);
}

// every scrap of text that might name this field
function fieldContext(el) {
  const bits = [
    el.name, el.id, el.placeholder, el.getAttribute('aria-label'),
    el.getAttribute('data-testid'), el.getAttribute('data-field'),
    el.closest('label')?.innerText,
    el.id ? document.querySelector(`label[for="${CSS.escape(el.id)}"]`)?.innerText : '',
    el.previousElementSibling?.innerText,
    el.parentElement?.previousElementSibling?.innerText,
    el.closest('div,li,fieldset,tr')?.firstElementChild?.innerText,
  ];
  return bits.filter(Boolean).join(' ').toLowerCase().slice(0, 300);
}

// ORDER MATTERS: most specific first, 'title' LAST.
// A field named `criteria[0].justification` contains the substring "criteri",
// so a greedy title pattern checked first would swallow every field in the row
// and collapse the whole form into one role. Distinctive roles claim their
// fields first; title is the fallback for whatever is left.
const ROLE_PATTERNS = [
  ['justification', /justif|rationale|reason|why/],
  ['evidence',      /evidence|how to (check|verify)|grading|verification|what to look/],
  ['category',      /categor|\btype\b|\bkind\b/],
  ['title',         /criteri|title|rubric name|statement|description of/],
];

function roleOf(el) {
  const ctx = fieldContext(el);
  for (const [role, re] of ROLE_PATTERNS) if (re.test(ctx)) return role;
  if (el.tagName === 'SELECT') return 'category';
  return null;
}

// group flat field list into one group per rubric
function groupFields(fields, forcedSize) {
  const roles = fields.map(roleOf);

  if (!forcedSize && roles.filter(Boolean).length >= fields.length * 0.5) {
    // role-based: start a new group whenever a role repeats
    const groups = [];
    let cur = {}, curEls = [];
    fields.forEach((el, i) => {
      const r = roles[i];
      if (r && cur[r] !== undefined) { groups.push({ map: cur, els: curEls }); cur = {}; curEls = []; }
      if (r) cur[r] = el;
      curEls.push(el);
    });
    if (curEls.length) groups.push({ map: cur, els: curEls });
    return { groups, mode: 'role' };
  }

  // positional fallback: fixed-size chunks, mapped by order
  const size = forcedSize || 3;
  const order = ['title', 'justification', 'evidence', 'category'];
  const groups = [];
  for (let i = 0; i + size <= fields.length; i += size) {
    const els = fields.slice(i, i + size);
    const map = {};
    els.forEach((el, j) => { if (order[j]) map[order[j]] = el; });
    groups.push({ map, els });
  }
  return { groups, mode: `positional(size=${size})` };
}

// ---------- PROBE ---------------------------------------------
function PROBE() {
  const fields = allFields();
  console.log(`%c${fields.length} editable fields visible`, 'font-weight:bold;font-size:13px');
  console.table(fields.map((el, i) => ({
    i, tag: el.tagName.toLowerCase(), type: el.type || (el.isContentEditable ? 'contenteditable' : ''),
    detectedRole: roleOf(el) || '-',
    name: el.name || '', placeholder: (el.placeholder || '').slice(0, 30),
    testid: el.getAttribute('data-testid') || '',
    ctx: fieldContext(el).slice(0, 60),
    value: (el.value ?? el.innerText ?? '').slice(0, 25),
  })));

  const { groups, mode } = groupFields(fields);
  console.log(`grouping mode: %c${mode}%c -> ${groups.length} group(s) detected, need ${RUBRICS.length}`,
              'font-weight:bold', '');
  if (groups[0]) console.log('first group maps:', Object.fromEntries(
    Object.entries(groups[0].map).map(([k, v]) => [k, v.tagName.toLowerCase() + (v.name ? `[name=${v.name}]` : '')])));

  const addBtns = [...document.querySelectorAll('button,[role=button],a')]
    .filter(visible).filter(b => /add|new criter|new rubric|\+\s*$/i.test(b.innerText || ''));
  console.log('candidate "add row" controls:', addBtns.map(b => (b.innerText || '').trim().slice(0, 40)));
  window.__addBtns = addBtns;
  console.log('-> if one of those is the add button: ADD_BTN = __addBtns[0]');
  return { fields, groups };
}

// ---------- row creation --------------------------------------
let ADD_BTN = null;
async function ENSURE_ROWS(target = RUBRICS.length, {maxClicks = 200} = {}) {
  if (!ADD_BTN) { console.warn('Set ADD_BTN first (run PROBE, then ADD_BTN = __addBtns[0]).'); return; }
  let clicks = 0;
  let n = groupFields(allFields()).groups.length;
  while (n < target && clicks < maxClicks) {
    ADD_BTN.click();
    await sleep(180);
    const next = groupFields(allFields()).groups.length;
    if (next === n) { console.warn(`row count stuck at ${n} after click ${clicks + 1}; stopping`); break; }
    n = next; clicks++;
  }
  console.log(`rows now: ${n} (target ${target}, ${clicks} clicks)`);
  return n;
}

// ---------- FILL ----------------------------------------------
async function FILL({ dryRun = false, start = 0, size = null, delay = 60 } = {}) {
  const { groups, mode } = groupFields(allFields(), size);
  console.log(`mode ${mode} | groups ${groups.length} | rubrics ${RUBRICS.length}`);
  if (groups.length < RUBRICS.length) {
    console.warn(`Only ${groups.length} rows for ${RUBRICS.length} rubrics. ` +
                 `Run ENSURE_ROWS() first, or fill in passes with {start:N}.`);
  }
  let written = 0, missing = [];
  const n = Math.min(groups.length, RUBRICS.length - start);
  for (let i = 0; i < n; i++) {
    const r = RUBRICS[start + i], g = groups[i].map;
    for (const key of ['title', 'justification', 'evidence', 'category']) {
      const el = g[key], val = r[key];
      if (val == null) continue;
      if (!el) { missing.push(`row ${start + i}: no ${key} field`); continue; }
      if (dryRun) { console.log(`row ${start + i} .${key} <- ${String(val).slice(0, 70)}`); continue; }
      if (el.tagName === 'SELECT') {
        const opt = [...el.options].find(o => o.value.toLowerCase() === String(val).toLowerCase()
                                           || o.text.toLowerCase().includes(String(val).toLowerCase()));
        if (opt) setNativeValue(el, opt.value); else missing.push(`row ${start + i}: no option "${val}"`);
      } else setNativeValue(el, val);
    }
    written++;
    if (!dryRun) await sleep(delay);
  }
  if (missing.length) console.warn('gaps:', missing.slice(0, 20));
  console.log(`%c${dryRun ? 'DRY RUN' : 'done'}: ${written} rows`, 'color:green;font-weight:bold');
  if (!dryRun) console.log('Now run VERIFY() before you submit.');
}

// ---------- VERIFY --------------------------------------------
function VERIFY({ start = 0, size = null } = {}) {
  const { groups } = groupFields(allFields(), size);
  const bad = [];
  for (let i = 0; i < Math.min(groups.length, RUBRICS.length - start); i++) {
    const r = RUBRICS[start + i], g = groups[i].map;
    for (const key of ['title', 'justification', 'evidence']) {
      const got = (g[key]?.value ?? g[key]?.innerText ?? '').trim();
      const want = (r[key] ?? '').trim();
      if (want && got !== want) bad.push({ row: start + i, field: key,
        want: want.slice(0, 45), got: (got || '<empty>').slice(0, 45) });
    }
  }
  if (!bad.length) console.log(`%call ${Math.min(groups.length, RUBRICS.length)} rows match source JSON`,
                               'color:green;font-weight:bold');
  else { console.warn(`${bad.length} mismatches`); console.table(bad); }
  return bad;
}

console.log('%cRubric filler loaded (' + RUBRICS.length + ' criteria).', 'font-weight:bold;font-size:13px');
console.log('Run:  PROBE()   ->  FILL({dryRun:true})  ->  FILL()  ->  VERIFY()');
"""

out = (TEMPLATE.replace("@@PAYLOAD@@", payload)
               .replace("@@N@@", str(len(rubrics)))
               .replace("@@SRC@@", str(src)))
print(out)
