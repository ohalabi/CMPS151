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

#### Option B - no Git, just download

1. Go to [github.com/ohalabi/CMPS151](https://github.com/ohalabi/CMPS151)
2. Click the green **Code** button, then **Download ZIP**.
3. Unzip it anywhere on your computer.
4. Note: with this option you'll need to repeat the download every time you want new chapters (see below), and it won't track your own edits.

### 2. Get new chapters after they're uploaded

I push each chapter's notebook right after we cover it in class. To get the latest files:

#### If you used `git clone` (Option A)

1. Open a terminal in your `CMPS151` folder.
2. Run:

   ```bash
   git pull
   ```

3. Any new or updated chapter files will download automatically.

Important: if you've been editing the chapter notebooks directly (adding your own answers, notes, etc.), `git pull` can fail or create conflicts when I update that same file. To avoid this:

- Keep your own work in a separate file/folder (e.g., copy a notebook to `my_notes_chp2.ipynb` before editing), **or**
- Before pulling, save your changes with:

  ```bash
  git add .
  git commit -m "my work"
  ```

  then run `git pull`.

#### If you downloaded the ZIP (Option B)

1. Go back to [github.com/ohalabi/CMPS151](https://github.com/ohalabi/CMPS151) and download the ZIP again.
2. Unzip it, and copy over just the new chapter file(s) you don't have yet - don't overwrite files you've already been editing, or you'll lose your changes.
