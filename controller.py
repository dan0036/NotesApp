import model
from model import *
import view

notes = list()
last_id = 0
def start():

    model.refresh()
    print(text.open_successful)


    while True:
        choice = view.main_menu()
        match choice:
            case '1':
                print(text.view_note_by_date)
                if view.choice_switch():
                    date = input(text.ask_input_date)
                    model.list_notes(notes, date)
                else:
                    model.list_notes(notes)
            case '2': # add note
                title = input(text.input_new_note_title)
                msg = input(text.input_new_note_msg)
                model.add_note(title, msg, notes)
                model.refresh()
            case '3': # find note
                find = input(text.input_search_word)
                for e in model.find_note_by_text(find, notes):
                    print(e)
            case '4': # edit note
                id_edit = int(input(text.input_edit_id))
                title = input(text.input_edit_note_title)
                message = input(text.input_new_note_msg)
                model.edit_note(id_edit, title, message, notes)
                model.refresh()
            case '5': # delete note
                id_edit = int(input(text.input_delete_id))
                model.delete_note(id_edit, notes)
            case '6':
                break


