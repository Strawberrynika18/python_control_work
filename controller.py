import WorkinFile


def action_in_working():
    input_from_user = ''

    while True:
        WorkinFile.menu()
        input_from_user = input().strip()

        if input_from_user == '1':
            function.show('all')
            continue
        elif input_from_user == '2':
            function.add()
        elif input_from_user == '3':
            function.show('all')
            function.id_edit_del_show('del')
        elif input_from_user == '4':
            function.show('all')
            function.id_edit_del_show('edit')
        elif input_from_user == '5':
            function.show('date')
        elif input_from_user == '6':
            function.show('id')
            function.id_edit_del_show('show')
        elif input_from_user == '0':
            WorkinFile.goodbuy()
            break