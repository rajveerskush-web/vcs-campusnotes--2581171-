
import json
import os

FILE_NAME = "notes.json"


def load_notes():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


def save_notes(notes):
    with open(FILE_NAME, "w") as file:
        json.dump(notes, file, indent=4)


def add_note(notes):
    subject = input("Enter subject: ")
    content = input("Enter your note: ")

    notes.append({
        "subject": subject,
        "content": content
    })

    save_notes(notes)
    print("Note added successfully!")


def view_notes(notes):
    if not notes:
        print("No notes available.")
        return

    for i, note in enumerate(notes, start=1):
        print(f"\n{i}. Subject: {note['subject']}")
        print(f"   Note: {note['content']}")


def search_notes(notes):
    subject = input("Enter subject to search: ").lower()

    found = False

    for note in notes:
        if subject in note["subject"].lower():
            print(f"\nSubject: {note['subject']}")
            print(f"Note: {note['content']}")
            found = True

    if not found:
        print("No matching notes found.")


def delete_note(notes):
    view_notes(notes)

    if not notes:
        return

    try:
        number = int(input("\nEnter note number to delete: "))

        if 1 <= number <= len(notes):
            removed = notes.pop(number - 1)
            save_notes(notes)
            print(f"Deleted note: {removed['subject']}")
        else:
            print("Invalid note number.")

    except ValueError:
        print("Please enter a valid number.")


def main():
    notes = load_notes()

    while True:
        print("\n===== CAMPUS NOTES =====")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Search Notes")
        print("4. Delete Note")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_note(notes)
        elif choice == "2":
            view_notes(notes)
        elif choice == "3":
            search_notes(notes)
        elif choice == "4":
            delete_note(notes)
        elif choice == "5":
            print("Thank you for using CampusNotes!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
