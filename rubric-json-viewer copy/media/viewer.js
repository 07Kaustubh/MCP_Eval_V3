// @ts-check
(function () {
  const vscode = acquireVsCodeApi();

  /** @type {Record<string, unknown>[]} */
  let items = [];
  let index = 0;
  /** @type {string} */
  let sourceLabel = "";

  const formRoot = document.getElementById("formRoot");
  const counterEl = document.getElementById("counter");
  const prevBtn = document.getElementById("prev");
  const nextBtn = document.getElementById("next");
  const sourceEl = document.getElementById("sourceLabel");
  const toastEl = document.getElementById("toast");
  /** @type {ReturnType<typeof setTimeout> | null} */
  let toastTimer = null;

  function showToast(message) {
    if (!toastEl) return;
    toastEl.textContent = message;
    toastEl.classList.add("toast--show");
    if (toastTimer) clearTimeout(toastTimer);
    toastTimer = setTimeout(() => {
      toastEl.classList.remove("toast--show");
      toastTimer = null;
    }, 2200);
  }

  function formatValue(value) {
    if (value === null) return "null";
    if (value === undefined) return "";
    if (typeof value === "object") {
      try {
        return JSON.stringify(value, null, 2);
      } catch {
        return String(value);
      }
    }
    return String(value);
  }

  function copyIconSvg() {
    return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>`;
  }

  /** @param {string[]} keys */
  function findIdKey(keys) {
    const order = ["Rubric_Id", "rubric_id", "id"];
    for (const want of order) {
      const found = keys.find((k) => k.toLowerCase() === want.toLowerCase());
      if (found) return found;
    }
    return undefined;
  }

  /** @param {string[]} keys */
  function findCategoryKey(keys) {
    return keys.find((k) => k.toLowerCase() === "category");
  }

  function render() {
    if (!formRoot || !counterEl || !prevBtn || !nextBtn) return;

    const n = items.length;
    if (n === 0) {
      formRoot.innerHTML = "<p>No items.</p>";
      counterEl.textContent = "";
      prevBtn.disabled = true;
      nextBtn.disabled = true;
      return;
    }

    index = Math.max(0, Math.min(index, n - 1));
    const obj = items[index];

    counterEl.textContent = `${index + 1} / ${n}`;
    prevBtn.disabled = index <= 0;
    nextBtn.disabled = index >= n - 1;

    const allKeys = Object.keys(obj);
    const idKey = findIdKey(allKeys);
    const catKey = findCategoryKey(allKeys);
    const mergeIdCategory = Boolean(
      idKey && catKey && idKey !== catKey && Object.prototype.hasOwnProperty.call(obj, idKey) && Object.prototype.hasOwnProperty.call(obj, catKey)
    );

    const keys = allKeys
      .filter((k) => !mergeIdCategory || (k !== idKey && k !== catKey))
      .sort((a, b) => b.localeCompare(a));
    formRoot.innerHTML = "";

    let i = 0;

    if (mergeIdCategory && idKey && catKey) {
      const idText = formatValue(obj[idKey]);
      const catText = formatValue(obj[catKey]);
      const copyText = `${idKey}: ${idText}\n${catKey}: ${catText}`;
      const fieldId = `f-${index}-${i}`;
      const field = document.createElement("div");
      field.className = "field field--meta";
      field.innerHTML = `
        <div class="field-header field-header--meta">
          <div class="meta-row" role="group" aria-label="Identifier and category">
            <span class="meta-kv">
              <span class="meta-key">${escapeHtml(idKey)}</span><span class="meta-colon">:</span>
              <span class="meta-val" id="${fieldId}-id">${escapeHtml(idText)}</span>
            </span>
            <span class="meta-sep" aria-hidden="true">·</span>
            <span class="meta-kv">
              <span class="meta-key">${escapeHtml(catKey)}</span><span class="meta-colon">:</span>
              <span class="meta-val" id="${fieldId}-cat">${escapeHtml(catText)}</span>
            </span>
          </div>
          <button type="button" class="copy-btn" title="Copy id and category">${copyIconSvg()}</button>
        </div>
      `;
      const btn = field.querySelector(".copy-btn");
      btn?.addEventListener("click", () => {
        vscode.postMessage({ type: "copy", text: copyText, fieldLabel: `${idKey} + ${catKey}` });
      });
      const metaRow = field.querySelector(".meta-row");
      metaRow?.addEventListener("dblclick", () => {
        vscode.postMessage({ type: "copy", text: copyText, fieldLabel: `${idKey} + ${catKey}` });
      });
      formRoot.appendChild(field);
      i += 1;
    }

    keys.forEach((key) => {
      const text = formatValue(obj[key]);
      const fieldId = `f-${index}-${i}`;
      const field = document.createElement("div");
      field.className = "field";
      field.innerHTML = `
        <div class="field-header">
          <label class="field-label" for="${fieldId}">${escapeHtml(key)}</label>
          <button type="button" class="copy-btn" title="Copy value">${copyIconSvg()}</button>
        </div>
        <textarea class="field-value" id="${fieldId}" readonly rows="${textareaRows(text)}">${escapeHtml(text)}</textarea>
      `;
      const btn = field.querySelector(".copy-btn");
      const ta = field.querySelector(".field-value");
      btn?.addEventListener("click", () => {
        vscode.postMessage({ type: "copy", text, fieldLabel: key });
      });
      ta?.addEventListener("dblclick", () => {
        vscode.postMessage({ type: "copy", text, fieldLabel: key });
      });
      formRoot.appendChild(field);
      i += 1;
    });
  }

  function textareaRows(text) {
    const lines = text.split("\n").length;
    return Math.min(24, Math.max(3, lines));
  }

  function escapeHtml(s) {
    return s
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;");
  }

  prevBtn?.addEventListener("click", () => {
    if (index > 0) {
      index -= 1;
      render();
    }
  });

  nextBtn?.addEventListener("click", () => {
    if (index < items.length - 1) {
      index += 1;
      render();
    }
  });

  window.addEventListener("keydown", (e) => {
    if (e.key === "ArrowLeft" && !e.shiftKey && !e.altKey && !e.metaKey && !e.ctrlKey) {
      prevBtn?.click();
    } else if (e.key === "ArrowRight" && !e.shiftKey && !e.altKey && !e.metaKey && !e.ctrlKey) {
      nextBtn?.click();
    }
  });

  window.addEventListener("message", (event) => {
    const msg = event.data;
    if (msg?.type === "init" && Array.isArray(msg.items)) {
      items = msg.items;
      index = 0;
      sourceLabel = typeof msg.sourceLabel === "string" ? msg.sourceLabel : "";
      if (sourceEl && sourceLabel) sourceEl.textContent = sourceLabel;
      render();
      return;
    }
    if (msg?.type === "copied") {
      const label = typeof msg.fieldLabel === "string" ? msg.fieldLabel.trim() : "";
      showToast(label ? `Copied: ${label}` : "Copied to clipboard");
    }
  });

  vscode.postMessage({ type: "ready" });
})();
