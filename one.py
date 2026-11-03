"""
PS 64 - Digital Notes Management System
Language : Python 3
Concepts : Strings, Files, Search, CRUD

Notes are stored in notes.txt, one note per line, in the format:
    ID|Title|Content
Example:
    N1|Python|Learn loops
"""

import os

FILE_NAME = "notes.txt"
SEPARATOR = "|"


# ----------------------------------------------------------------------
# FILE HANDLING  (load / save)
# ----------------------------------------------------------------------
def load_notes():
    """Read notes.txt and return a list of dictionaries.

    Each dictionary looks like: {"id": "N1", "title": "Python", "content": "Learn loops"}
    If the file does not exist yet, an empty list is returned.
    """
    notes = []
    if not os.path.exists(FILE_NAME):
        return notes

    with open(FILE_NAME, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()                      # remove '\n' and extra spaces
            if line == "":                           # skip blank lines
                continue
            parts = line.split(SEPARATOR, 2)         # split into at most 3 parts
            if len(parts) != 3:                      # skip corrupted lines
                continue
            notes.append({
                "id": parts[0].strip(),
                "title": parts[1].strip(),
                "content": parts[2].strip(),
            })
    return notes


def save_notes(notes):
    """Write the whole list of notes back to notes.txt (overwrites the file)."""
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        for note in notes:
            file.write(note["id"] + SEPARATOR + note["title"] + SEPARATOR
                       + note["content"] + "\n")


# ----------------------------------------------------------------------
# HELPER FUNCTIONS
# ----------------------------------------------------------------------
def clean_text(text):
    """Strip spaces and replace the '|' character so it cannot break the file format."""
    return text.strip().replace(SEPARATOR, "/")


def generate_id(notes):
    """Return the next ID: N1 for the first note, otherwise (highest number + 1).

    Using the highest number (not the count) prevents re-using the ID of a deleted note.
    """
    highest = 0
    for note in notes:
        number_part = note["id"][1:]                 # 'N12' -> '12'
        if number_part.isdigit() and int(number_part) > highest:
            highest = int(number_part)
    return "N" + str(highest + 1)


def find_note(notes, note_id):
    """Return the note with the given ID (case-insensitive) or None."""
    for note in notes:
        if note["id"].lower() == note_id.strip().lower():
            return note
    return None


# ----------------------------------------------------------------------
# CRUD OPERATIONS
# ----------------------------------------------------------------------
def add_note():
    """CREATE - add a new note."""
    notes = load_notes()
    title = clean_text(input("Title: "))
    content = clean_text(input("Content: "))

    if title == "":                                  # validation: empty title
        print("Title cannot be empty. Note not saved.")
        return

    new_id = generate_id(notes)
    notes.append({"id": new_id, "title": title, "content": content})
    save_notes(notes)
    print("Note saved. ID: " + new_id + " | " + title)


def view_notes():
    """READ - show all notes."""
    notes = load_notes()
    if len(notes) == 0:
        print("No notes found.")
        return
    for note in notes:
        print(note["id"] + " | " + note["title"] + " | " + note["content"])


def search_notes():
    """SEARCH - case-insensitive keyword search in title AND content."""
    notes = load_notes()
    keyword = input("Keyword: ").strip().lower()

    if keyword == "":
        print("Keyword cannot be empty.")
        return

    found = 0
    for note in notes:
        if keyword in note["title"].lower() or keyword in note["content"].lower():
            print(note["id"] + " | " + note["title"] + " | " + note["content"])
            found += 1

    if found == 0:
        print("No matching notes found.")


def edit_note():
    """UPDATE - change the content (and optionally the title) of a note."""
    notes = load_notes()
    note_id = input("Note ID: ").strip()
    note = find_note(notes, note_id)

    if note is None:
        print("Note " + note_id.upper() + " not found.")
        return

    new_content = clean_text(input("New content: "))
    new_title = clean_text(input("New title (press Enter to keep old): "))

    note["content"] = new_content
    if new_title != "":
        note["title"] = new_title

    save_notes(notes)
    print("Note " + note["id"] + " updated.")


def delete_note():
    """DELETE - remove a note by ID."""
    notes = load_notes()
    note_id = input("Note ID: ").strip()
    note = find_note(notes, note_id)

    if note is None:
        print("Note " + note_id.upper() + " not found.")
        return

    notes.remove(note)
    save_notes(notes)
    print("Note " + note["id"] + " deleted. Notes left: " + str(len(notes)))


# ----------------------------------------------------------------------
# MAIN MENU
# ----------------------------------------------------------------------
def show_menu():
    print("\n===== DIGITAL NOTES MANAGEMENT SYSTEM =====")
    print("1. Add note")
    print("2. View all notes")
    print("3. Search notes")
    print("4. Edit note")
    print("5. Delete note")
    print("6. Exit")


def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            search_notes()
        elif choice == "4":
            edit_note()
        elif choice == "5":
            delete_note()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()
