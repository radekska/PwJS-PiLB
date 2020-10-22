import json

def print_menu():
    print('Wcisnij: ')
    print('1 - Dodaj recenzję.')
    print('2 - Usuń recenzję.')
    print('3 - Wyświetl recenzję')
    print('4 - Wyświetl wszystkie')
    print('Q - Zakończ program.')

    choice = input('Wybór: ')
    return choice

def add_entry(database):
    id = input('Podaj id: ')
    id = validator(database, id, action='add')
    if id is False:
        return None

    nazwa_filmu = input('Podaj nazwę filmu: ')
    ocena = input('Podaj ocenę (1 do 10): ')
    recenzja = input('Wpisz recenzję: ')

    entry = {
        'id': id,
        'nazwa_filmu' : nazwa_filmu,
        'ocena' : ocena,
        'recenzja' : recenzja
    }

    database['recenzje_filmow'].append(entry)
    return database

def remove_entry(database):
    id = input('Podaj id: ')
    id = validator(database, id, action='remove')
    if id is False:
        return None

    database['recenzje_filmow'] = list(filter(lambda item: item['id'] != id, database['recenzje_filmow']))
    print('Obiekt o id - {id} - usunięty.'.format(id=id))
    return database

def show_entry(database):
    id = input('Podaj id: ')
    id = validator(database, id, action='show')
    if id is False:
        return None

    print(id)
    show_object = list(filter(lambda item: item['id'] == id, database['recenzje_filmow']))[0]
    
    for key, value in show_object.items():
            print('{key} - {value}'.format(key=key, value=value))


def show_all_entries(database):
    if len(database) > 0:
        database = database['recenzje_filmow']
        for item in database:
            print('===========================')
            for key, value in item.items():
                print('{key} : {value}'.format(key=key, value=value))
            print('===========================')
    else:
        print('Baza danych jest pusta.')


    

def save_database(database):
    with open('json_dane/database.json', 'w') as file_stream:
        json.dump(database, file_stream)

def load_database():
    with open('json_dane/database.json', 'r') as file_stream:
        return json.loads(file_stream.read())

def validator(database, id, action='add'):
    database = database['recenzje_filmow']
    database_length = len(database)
    while True:
        if database_length == 0 and (action == 'remove' or action == 'show'):
            print('Baza danych jest pusta.')
            return False
        else:
            for item in database:
                item_values = list(item.values())[0]
                if id is item_values and action == 'add' :
                    print('Obiekt o podanym id juz istnieje.')
                    return False
          
                elif id is item_values and (action == 'remove' or action == 'show'):
                    return id
        
            if action == 'add':
                return id

            print('Nie znaleziono obiektu.')
            return False

def manage_actions():
    database = load_database()

    while True:
        choice = print_menu()
        if choice == '1':
            database_temp = add_entry(database)
            if database is not None:
                save_database(database_temp)
        elif choice == '2':
            database_temp = remove_entry(database)
            if database is not None:
                save_database(database_temp)
        elif choice == '3':
            show_entry(database)
        elif choice == '4':
            show_all_entries(database)
        elif choice in 'Qq':
            save_database(database)
            break


if __name__ == '__main__':
    manage_actions()