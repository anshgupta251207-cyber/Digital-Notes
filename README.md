# Digital Notes Management System

**PS No. 64** · Python 3 console application

A simple console program to **write, view, search, edit and delete text notes**. Every note has an ID, a title and its content, and all notes are saved permanently in a text file (`notes.txt`), so they are still there the next time the program runs.

**Concepts used:** Strings · Files · Search · CRUD

---

## Features

- **Add** a note with a title and content (IDs are generated automatically: N1, N2, N3, ...)
- **View** all saved notes
- **Search** notes by keyword (case-insensitive, checks both title and content)
- **Edit** a note by its ID
- **Delete** a note by its ID
- **Permanent storage** in `notes.txt`, loaded again every time the program starts
- **Validation**: empty titles are rejected, and a clear message is shown when a note ID does not exist

---

## Requirements

- Python 3.6 or later
- No external libraries (only the built-in `os` module is used)

---

## How to Run

1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run:

```bash
python notes_manager.py
```

On some systems use `python3 notes_manager.py` instead.

`notes.txt` is created automatically the first time you add a note.

---

## Menu

```
===== DIGITAL NOTES MANAGEMENT SYSTEM =====
1. Add note
2. View all notes
3. Search notes
4. Edit note
5. Delete note
6. Exit
```

| Option | Action | What happens |
|---|---|---|
| 1 | Add note | Asks for a title and content, then saves the note with a new ID |
| 2 | View all notes | Prints every note as `ID \| Title \| Content` |
| 3 | Search notes | Asks for a keyword and prints every matching note |
| 4 | Edit note | Asks for an ID and new content (new title is optional, press Enter to keep the old one) |
| 5 | Delete note | Asks for an ID and removes that note |
| 6 | Exit | Closes the program |

---

## File Format

Notes are stored in `notes.txt`, **one note per line**, in the format `ID|Title|Content`:

```
N1|Python|Learn loops
N2|Maths|Revise algebra
```

- The first note always gets the ID `N1`.
- A new ID is `N` + (highest existing number + 1), so the ID of a deleted note is never reused.
- If you type a `|` character in a title or content, it is replaced with `/` so it cannot break the file format.

---

## Sample Run

```
Choose an option (1-6): 1
Title: Python
Content: Learn loops
Note saved. ID: N1 | Python

Choose an option (1-6): 3
Keyword: PYTHON
N1 | Python | Learn loops

Choose an option (1-6): 4
Note ID: N1
New content: Practice loops daily
New title (press Enter to keep old):
Note N1 updated.

Choose an option (1-6): 5
Note ID: N1
Note N1 deleted. Notes left: 0

Choose an option (1-6): 2
No notes found.
```

---

## Test Cases

| # | Scenario | Input | Expected output |
|---|---|---|---|
| 1 | Normal input | Option 1, Title: `Python`, Content: `Learn loops` | `Note saved. ID: N1 \| Python` |
| 2 | Boundary / minimum | `notes.txt` is empty, option 2 | `No notes found.` |
| 3 | Invalid input | Option 1, empty title, Content: `Buy books` | `Title cannot be empty. Note not saved.` |
| 4 | Different valid scenario | `notes.txt` has N1 and N2; (a) search `python`, (b) edit N2 to `Revise calculus`, (c) delete N1 | (a) `N1 \| Python \| Learn loops`<br>(b) `Note N2 updated.`<br>(c) `Note N1 deleted. Notes left: 1` |

All four test cases pass.

---

## Project Structure

```
.
├── notes_manager.py   # the complete program (single file)
├── notes.txt          # notes storage (created automatically)
└── README.md          # this file
```

---

## How the Code Works

| Function | Purpose |
|---|---|
| `load_notes()` | Reads `notes.txt` and returns a list of note dictionaries |
| `save_notes(notes)` | Writes the list of notes back to `notes.txt` |
| `clean_text(text)` | Strips spaces and replaces `\|` so the file format stays safe |
| `generate_id(notes)` | Creates the next ID (N1, N2, ...) |
| `find_note(notes, note_id)` | Finds a note by ID, ignoring upper/lower case |
| `add_note()` | **Create**: adds a new note |
| `view_notes()` | **Read**: shows all notes |
| `search_notes()` | **Search**: finds notes by keyword |
| `edit_note()` | **Update**: changes an existing note |
| `delete_note()` | **Delete**: removes a note |
| `main()` | Shows the menu in a loop and calls the right function |

### Concepts in the project

- **Strings**: `strip()`, `split("|", 2)`, `lower()`, `in`, `replace()` and `isdigit()` are used to read lines from the file, clean input and match search keywords.
- **Files**: `open()` with the `with` statement reads and writes `notes.txt`; `os.path.exists()` avoids an error when the file does not exist yet.
- **Search**: both the keyword and the note text are converted to lowercase, then checked with `in`, so searching `python` finds `Python`.
- **CRUD**: Create (`add_note`), Read (`view_notes`), Update (`edit_note`) and Delete (`delete_note`), each in its own function.

---

## Possible Improvements

- Add dates and timestamps to notes
- Add categories or tags
- Export notes to a different format (CSV or PDF)
- Add a simple graphical interface

---

## Author

Your Name · Your Roll Number / Class · Your College

*Replace the line above with your own details before uploading to GitHub.*
