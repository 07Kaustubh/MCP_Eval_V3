# Rubric JSON Viewer (local Cursor / VS Code extension)

Opens a JSON file whose root is an **array of objects** (or a single object). Shows one object at a time with **Prev / Next** (or **← / →** keys). Each property is a read-only field with a **copy** button (double-click the textarea also copies).

## Install in Cursor

1. Compile once: `npm install && npm run compile` in this folder.
2. **Cursor** → **Extensions** → **`⋯`** menu → **Install from VSIX…** is for VSIX; for a folder use:
   - **Command Palette** (`Cmd+Shift+P`) → **Developer: Install Extension from Location…**
   - Choose this folder: `rubric-json-viewer` (the one containing `package.json`).
3. Reload the window if prompted.

## Use

- **Command Palette** → **Rubric JSON Viewer: Open JSON File…**  
  - If `Tasks/updated_rubrics.json` exists in the workspace root, it opens that automatically.  
  - Otherwise you get a file picker.
- **Rubric JSON Viewer: Open Active JSON** — uses the file in the current editor.

## Settings

`rubricJsonViewer.defaultRelativePath` — workspace-relative path for the quick-open command (default: `Tasks/updated_rubrics.json`).

## Dev

```bash
npm run watch
```

Then **Run Extension** from this folder in VS Code/Cursor (F5) to debug in a new window.
