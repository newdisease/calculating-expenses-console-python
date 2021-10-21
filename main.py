import sqlite3
from sqlite3 import Error
from methods import clear_data, add_db, add_category, add_purchase, show_all_categories, show_all_expenses, \
    show_expenses_by_category


def help_command():
    for key, value in commands.items():
        print(f'"{key}" for {value}')


commands = {
    0: 'clear_data',
    1: 'add_purchase',
    2: 'show_all_expenses',
    3: 'show_expenses_by_category',
    4: 'show_all_categories',
    5: 'add_category',

}

commands_methods = {
    0: clear_data,
    1: add_purchase,
    2: show_all_expenses,
    3: show_expenses_by_category,
    4: show_all_categories,
    5: add_category,

}


def create_connection(db_file):
    connection = None
    try:
        connection = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return connection


def main():
    database = 'money_tracking.db'

    # create a database connection
    connection = create_connection(database)
    with connection:
        add_db(connection)
        try:
            command = int(input('Type a number (1-5) or "6" for help or any other button for exit\n'))
            if command == 6:
                help_command()
            else:
                commands_methods[command](connection)
            main()
        except ValueError:
            print('App has been closed')


if __name__ == '__main__':
    main()
