import sqlite3
from datetime import datetime


def add_db(connection):
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS categories (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category TEXT NOT NULL UNIQUE 
        )""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        time CURRENT_TIMESTAMP,
        category_id INTEGER NOT NULL,
        price INTEGER NOT NULL,
        FOREIGN KEY (category_id) REFERENCES categories(id)
        )""")


def clear_data(connection):
    cursor = connection.cursor()
    cursor.execute("""DELETE FROM categories""")
    cursor.execute("""DELETE FROM expenses""")


def add_category(connection):
    new_category = str(input('Type a category: ')).lower()
    cursor = connection.cursor()
    try:
        cursor.execute("INSERT INTO categories (category) VALUES (?)", (new_category,))
        print(f'Category "{new_category}" has been added')
    except sqlite3.IntegrityError:
        print("couldn't add category twice")


def add_purchase(connection):
    category_name = str(input('Type a category(name): '))
    new_purchase = int(input('Type an expenses(number): '))
    time = datetime.today()

    cursor = connection.cursor()
    try:
        cursor.execute(
            """SELECT id FROM categories WHERE category == (?)""", (category_name,))
        category_id = cursor.fetchall()[0][0]  # unpacking tuple (can get just one category)
        cursor.execute(
            """INSERT INTO expenses (price, category_id, time) VALUES (?, ?, ?)""",
            (new_purchase, category_id, time))
    except IndexError:
        print('NO SUCH CATEGORY! Type "7" to add new category')


def show_all_categories(connection):
    cursor = connection.cursor()

    cursor.execute(
        """SELECT * FROM categories""")

    categories = cursor.fetchall()
    for category in categories:
        print(*category)


def show_all_expenses(connection):
    all_expenses = 0
    cursor = connection.cursor()
    cursor.execute(
        """SELECT price FROM expenses""")
    for price in cursor.fetchall():
        all_expenses += price[0]
    print(f'All expenses — {all_expenses}')


def show_expenses_by_category(connection):
    expenses = 0
    category = input('Type a category: ')
    cursor = connection.cursor()
    cursor.execute(
        """SELECT id FROM categories WHERE category == (?)""", (category,))
    category_id = cursor.fetchall()[0][0]
    cursor.execute(
        """SELECT price FROM expenses WHERE category_id == (?)""", (category_id,))
    for price in cursor.fetchall():
        expenses += price[0]
    print(f'Expenses by category "{category}" — {expenses}')
