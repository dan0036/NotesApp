import json
from datetime import datetime

import controller
import text


def load_notes(filename='notes.json'):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def load_last_id(notes: list):
    return notes[len(notes) - 1].get("id")


def refresh():
    controller.notes = load_notes()
    controller.last_id = load_last_id(controller.notes)


def save_notes(notes, filename='notes.json'):
    with open(filename, 'w') as file:
        json.dump(notes, file, indent=2)


def add_note(title, message, notes):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    controller.last_id += 1
    note = {'id': controller.last_id, 'title': title, 'message': message, 'timestamp': timestamp}
    notes.append(note)
    save_notes(notes)
    print('Note save successful')


def list_notes(notes, date_filter=None):
    if date_filter:
        filtered_notes = [note for note in notes if note['timestamp'].startswith(date_filter)]
    else:
        filtered_notes = notes

    print('*** NOTES start ***')
    for note in filtered_notes:
        print(f"{note['id']}. {note['title']} ({note['timestamp']})")
        print(note['message'])
    print('*** NOTES end ***')


def find_note_by_text(find: str, notes: list[dict]):
    found_notes = list()
    for note in notes:
        if find in (note.get('title') or note.get('message')):
            found_notes.append(note)
    if len(found_notes) > 0:
        return found_notes
    else:
        none_result = list()
        none_result.append(text.search_note_error(find))
        return none_result


def edit_note(note_id, title, message, notes: list):
    for note in notes:
        if note.get('id') == note_id:
            print('**'+title+'**')
            if title != '':
                note.update({'title': title})
            if message != '':
                note.update({'message': message})
            note.update({'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
            save_notes(notes)
            print('Note edition successful.')
            return
    print(f"Note with id {note_id} not found.")


def delete_note(note_id, notes):
    for note in notes:
        if note.get('id') == note_id:
            notes.remove(note)
            save_notes(notes)
            print('Note deletion successful.')
            return
    print(f"Note with id {note_id} not found.")
