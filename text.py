main_menu = ['Главное меню',
             'Показать все заметки',
             'Добавить заметку',
             'Найти заметку',
             'Изменить заметку',
             'Удалить заметку',
             'Выход']

input_main_menu = 'Выберите пункт меню: '
input_main_menu_error = f'Выберите пункт меню, число от 1 до {len(main_menu)-1}'

open_successful = 'Записная книжка успешно открыта.'
save_successful = 'Записная книга успешно сохранена.'

empty_note_book_error = 'Записная книга пуста или не открыта'

view_note_by_date = 'Хотите отобразить заметку по дате?'
ask_input_date = 'Введите дату в формате: yyyy-mm-dd:'

input_new_note_title = 'Введите заголовок заметки: '
input_new_note_msg = 'Введите текст заметки: '

input_search_word = 'Введите слово для поиска'

input_edit_note_title = 'Введите заголовок или Enter (без изменений): '
input_edit_note_msg = 'Введите текст заметки или Enter (без изменений): '

search_result_none = 'Заметка с искомым словом не найдена'

input_edit_word = 'Введите ключевое слово для поиска заметки, подлежащей изменению: '
input_delete_word = 'Введите ключевое слово для поиска заметки, подлежащей удалению: '

input_delete_id = 'Введите ID заметки, подлежащей удалению: '
input_edit_id = 'Введите ID заметки, подлежащей изменению: '

note_actions = ['сохранена', 'изменена', 'удалена']

confirm_delete_note = lambda x: f'Вы действительно хотите удалить заметку {x}? (y/n)'

confirm_changes = 'У вас есть несохраненные изменения! Сохранить? (y/n) '

good_bye = 'До свидания.'

def note_successful_result(name: str, mode: int) -> str:
    return f'Заметка {name} успешно {note_actions[mode]}.'

def search_note_error(word: str) -> str:
    return f'Заметки, содержащие {word}, не найдены.'

