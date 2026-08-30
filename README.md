# CMPS151 - Python Programming

Course materials for CMPS151, taught chapter by chapter throughout the semester.

## How this repo works

Content is added incrementally as it is covered in class - each chapter's
notebook and files are pushed here right after the corresponding lecture.
If a chapter isn't listed below yet, it hasn't been taught yet.

## Chapters

| # | Topic                                      |
| - | ------------------------------------------- |
| 1 | Introduction to Computers and Programming  |

More chapters will be added here as the semester progresses.

## For students: getting the code

### 1. Get the repo for the first time

#### Option A - using Git (recommended)

1. Install Git if you don't have it: [git-scm.com/downloads](https://git-scm.com/downloads)
2. Open a terminal (or Git Bash on Windows) in the folder where you want the class files to live.
3. Run:

   ```bash
   git clone https://github.com/ohalabi/CMPS151.git
   ```

4. This creates a `CMPS151` folder with all the current chapter notebooks inside it. Open that folder in VS Code or Jupyter to start working.

#### Option B - using VS Code's built-in Git (no terminal needed)

Since we're using VS Code for this course, you can clone straight from the editor:

1. Install Git if you don't have it: [git-scm.com/downloads](https://git-scm.com/downloads)
2. Open VS Code, press `Ctrl+Shift+P` to open the Command Palette, and type **Git: Clone**.
3. Paste the repo URL: `https://github.com/ohalabi/CMPS151.git`
4. Choose a folder to clone into, then click **Open** when VS Code asks if you want to open the cloned repo.

#### Option C - no Git, just download

1. Go to [github.com/ohalabi/CMPS151](https://github.com/ohalabi/CMPS151)
2. Click the green **Code** button, then **Download ZIP**.
3. Unzip it anywhere on your computer.
4. Note: with this option you'll need to repeat the download every time you want new chapters (see below), and it won't track your own edits.

### 2. Get new chapters after they're uploaded

I push each chapter's notebook right after we cover it in class. To get the latest files:

#### If you cloned with Git (Option A or B)

**Using a terminal:**

1. Open a terminal in your `CMPS151` folder.
2. Run:

   ```bash
   git pull
   ```

3. Any new or updated chapter files will download automatically.

**Using VS Code:**

1. Open the `CMPS151` folder in VS Code.
2. Click the **Source Control** icon in the left sidebar (or `Ctrl+Shift+G`).
3. Click the **...** menu at the top of the Source Control panel and choose **Pull** (or click the sync/refresh icon in the bottom status bar if you see one).

Important: if you've been editing the chapter notebooks directly (adding your own answers, notes, etc.), pulling can fail or create conflicts when I update that same file. To avoid this:

- Keep your own work in a separate file/folder (e.g., copy a notebook to `my_notes_chp2.ipynb` before editing), **or**
- Before pulling, save your changes first - in VS Code's Source Control panel, stage your changed files (`+`) and click **Commit**, then Pull. From a terminal:

  ```bash
  git add .
  git commit -m "my work"
  ```

  then run `git pull`.

#### If you downloaded the ZIP (Option C)

1. Go back to [github.com/ohalabi/CMPS151](https://github.com/ohalabi/CMPS151) and download the ZIP again.
2. Unzip it, and copy over just the new chapter file(s) you don't have yet - don't overwrite files you've already been editing, or you'll lose your changes.
