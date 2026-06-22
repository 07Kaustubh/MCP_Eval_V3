import * as vscode from "vscode";

const VIEW_TYPE = "rubricJsonViewer.panel";

function normalizeToObjectArray(parsed: unknown): Record<string, unknown>[] {
  if (Array.isArray(parsed)) {
    return parsed.map((item, i) => {
      if (item !== null && typeof item === "object" && !Array.isArray(item)) {
        return item as Record<string, unknown>;
      }
      return { _value: item, _index: i };
    });
  }
  if (parsed !== null && typeof parsed === "object" && !Array.isArray(parsed)) {
    return [parsed as Record<string, unknown>];
  }
  throw new Error("JSON root must be an object or an array of objects.");
}

async function loadJsonFromUri(uri: vscode.Uri): Promise<Record<string, unknown>[]> {
  const doc = await vscode.workspace.openTextDocument(uri);
  const text = doc.getText();
  const parsed = JSON.parse(text);
  return normalizeToObjectArray(parsed);
}

export function activate(context: vscode.ExtensionContext) {
  const openFromPath = async (fileUri: vscode.Uri) => {
    let items: Record<string, unknown>[];
    try {
      items = await loadJsonFromUri(fileUri);
    } catch (e) {
      const msg = e instanceof Error ? e.message : String(e);
      void vscode.window.showErrorMessage(`Rubric JSON Viewer: ${msg}`);
      return;
    }
    if (items.length === 0) {
      void vscode.window.showWarningMessage("Rubric JSON Viewer: JSON array is empty.");
      return;
    }
    showPanel(context, items, fileUri.fsPath);
  };

  context.subscriptions.push(
    vscode.commands.registerCommand("rubricJsonViewer.open", async () => {
      const config = vscode.workspace.getConfiguration("rubricJsonViewer");
      const rel = config.get<string>("defaultRelativePath")?.trim();
      const folders = vscode.workspace.workspaceFolders;

      if (folders?.length && rel) {
        const candidate = vscode.Uri.joinPath(folders[0].uri, rel);
        try {
          await vscode.workspace.fs.stat(candidate);
          await openFromPath(candidate);
          return;
        } catch {
          /* fall through to picker */
        }
      }

      const picked = await vscode.window.showOpenDialog({
        canSelectMany: false,
        openLabel: "Open",
        filters: { JSON: ["json"] },
      });
      if (picked?.[0]) {
        await openFromPath(picked[0]);
      }
    })
  );

  context.subscriptions.push(
    vscode.commands.registerCommand("rubricJsonViewer.openFromActiveFile", async () => {
      const editor = vscode.window.activeTextEditor;
      if (!editor) {
        void vscode.window.showErrorMessage("Rubric JSON Viewer: No active editor.");
        return;
      }
      const doc = editor.document;
      if (doc.languageId !== "json" && !doc.fileName.toLowerCase().endsWith(".json")) {
        void vscode.window.showWarningMessage(
          "Rubric JSON Viewer: Active file does not look like JSON. Save as .json or set language mode to JSON."
        );
      }
      await openFromPath(doc.uri);
    })
  );
}

function showPanel(
  context: vscode.ExtensionContext,
  items: Record<string, unknown>[],
  sourceLabel: string
) {
  const column = vscode.window.activeTextEditor?.viewColumn ?? vscode.ViewColumn.One;

  const panel = vscode.window.createWebviewPanel(
    VIEW_TYPE,
    "Rubric JSON Viewer",
    column,
    {
      enableScripts: true,
      retainContextWhenHidden: true,
      localResourceRoots: [vscode.Uri.joinPath(context.extensionUri, "media")],
    }
  );

  const scriptUri = panel.webview.asWebviewUri(
    vscode.Uri.joinPath(context.extensionUri, "media", "viewer.js")
  );
  const styleUri = panel.webview.asWebviewUri(
    vscode.Uri.joinPath(context.extensionUri, "media", "viewer.css")
  );

  const nonce = getNonce();

  panel.webview.html = getHtml(panel.webview.cspSource, nonce, scriptUri, styleUri, sourceLabel);

  panel.webview.onDidReceiveMessage(
    (message: { type: string; text?: string; fieldLabel?: string }) => {
      if (message.type === "ready") {
        panel.webview.postMessage({ type: "init", items, sourceLabel });
        return;
      }
      if (message.type === "copy" && typeof message.text === "string") {
        void vscode.env.clipboard.writeText(message.text).then(() => {
          panel.webview.postMessage({
            type: "copied",
            fieldLabel:
              typeof message.fieldLabel === "string" ? message.fieldLabel : undefined,
          });
        });
      }
    },
    undefined,
    context.subscriptions
  );
}

function getNonce(): string {
  let t = "";
  const c = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
  for (let i = 0; i < 32; i++) {
    t += c.charAt(Math.floor(Math.random() * c.length));
  }
  return t;
}

function getHtml(
  cspSource: string,
  nonce: string,
  scriptUri: vscode.Uri,
  styleUri: vscode.Uri,
  sourceLabel: string
): string {
  const esc = (s: string) =>
    s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/"/g, "&quot;");
  return `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta http-equiv="Content-Security-Policy" content="default-src 'none'; style-src ${cspSource} 'unsafe-inline'; script-src 'nonce-${nonce}' ${cspSource};" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <link href="${styleUri}" rel="stylesheet" />
  <title>Rubric JSON Viewer</title>
</head>
<body>
  <header class="header">
    <span class="source" id="sourceLabel">${esc(sourceLabel)}</span>
    <span class="counter" id="counter"></span>
  </header>
  <nav class="nav">
    <button type="button" id="prev" title="Previous (←)">← Prev</button>
    <button type="button" id="next" title="Next (→)">Next →</button>
  </nav>
  <main id="formRoot" class="form-root"></main>
  <div id="toast" class="toast" role="status" aria-live="polite" aria-atomic="true"></div>
  <script nonce="${nonce}" src="${scriptUri}"></script>
</body>
</html>`;
}

export function deactivate() {}
