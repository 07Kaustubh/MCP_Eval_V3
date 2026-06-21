# Rubric JSON Viewer — install & use (step by step)

You have a **folder** of extension files (unzip first if you got a `.zip`).

---

## Part 1 — One-time setup

### Step 1: Unzip

Unzip so you have a folder that contains **`package.json`** directly inside it (not nested in `rubric-json-viewer/rubric-json-viewer/` by accident).

### Step 2: Install Node (if you don’t have it)

You need **Node.js** for one command. Download from [nodejs.org](https://nodejs.org) (LTS is fine).

Check in Terminal:

```bash
node -v
npm -v
```

### Step 3: Build the extension

In Terminal, `cd` into that folder (the one with `package.json`), then run:

```bash
npm install
npm run compile
```

Wait until it finishes with no errors. This creates the `out/` folder Cursor needs.

### Step 4: Install the extension in Cursor

1. Open **Cursor**.
2. Press **`Cmd+Shift+P`** (Mac) or **`Ctrl+Shift+P`** (Windows/Linux).
3. Type: **`Install Extension from Location`**
4. Choose: **Developer: Install Extension from Location…**
5. Pick the **same folder** that contains `package.json` (not a parent folder).

### Step 5: Reload Cursor

- **`Cmd+Shift+P`** → **Developer: Reload Window**  
  (or restart Cursor.)

---

## Part 2 — Using it every day

### Open your rubrics (or any JSON)

**Option A — file already open**

1. Open your JSON file in Cursor (e.g. `Tasks/updated_rubrics.json`).
2. **`Cmd+Shift+P`** → **Rubric JSON Viewer: Open Active JSON**.

**Option B — from disk**

1. Open your project folder in Cursor (so the workspace root is your repo).
2. **`Cmd+Shift+P`** → **Rubric JSON Viewer: Open JSON File…**
3. If the file **`Tasks/updated_rubrics.json`** exists at the workspace root, it opens automatically; otherwise Cursor asks you to pick a `.json` file.

Your JSON must be either:

- an **array of objects** `[{ ... }, { ... }]`, or  
- a **single object** `{ ... }`.

### In the viewer

- **← Prev** / **Next →** (or arrow keys **←** / **→** when the viewer tab is focused) — move between objects.
- **Copy icon** next to a field, or **double-click** the text area — copies that value; a **toast** appears at the bottom.

---

## Check that it’s installed

Terminal:

```bash
cursor --list-extensions | grep rubric
```

You should see **`local.rubric-json-viewer`**.

Or **`Cmd+Shift+P`** and type **`Rubric JSON`** — you should see the two commands above.

---

## If something fails

| Problem | What to try |
|--------|----------------|
| No commands in palette | Reload window; confirm install picked the folder with `package.json`. |
| “Cannot find module” / empty panel | Run `npm install` and `npm run compile` again in the extension folder. |
| Wrong JSON file on “Open JSON File…” | In Cursor settings, search **`rubricJsonViewer.defaultRelativePath`** and set the path relative to your workspace root (default: `Tasks/updated_rubrics.json`). |

---

## Updating after you change the code

In the extension folder:

```bash
npm run compile
```

Then **Developer: Reload Window** in Cursor.
