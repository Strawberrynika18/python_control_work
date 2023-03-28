import Note

def create_note(number): #создание заметки
    title = check_len_text_input(input('Введите заголовок заметки: '), number)
    body = check_len_text_input(input('Введите описание заметки: '), number)
    return Note.Note(title=title, body=body)


def menu():
    print("Это программа 'Заметки'. Введите необходимую вам функцию:\n"
    "1 - вывод всех заметок из файла\n"
    "2 - добавление заметки\n"
    "3 - удаление заметки\n"
    "4 - редактирование заметки\n"
    "5 - выборка заметок по дате\n"
    "6 - показать заметку по id\n"
    "0 - выход\n ") 


def check_len_text_input(text, n):  #ограничение по кол-ву символов
    while len(text) >= n:
        print(f'Текст не должен превышать {n} символов')
        text = input('Введите текст в заметку: ')
    else:
        return text


def goodbye(): #выход
    print("Завершение работы программы 'заметки'. Будем рады видеть снова")