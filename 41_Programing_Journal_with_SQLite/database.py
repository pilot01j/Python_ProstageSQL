import sqlite3

connection = sqlite3.connect("data.db")
connection.row_factory = sqlite3.Row


def create_table():
    with connection:
        connection.execute("CREATE TABLE IF NOT EXISTS entries (content TEXT, date TEXT);")


def add_entry(entry_content, entry_date):
    with connection:
        connection.execute(
            # f"INSERT INTO entries VALUES ('{entry_content}', '{entry_date}');"
            "INSERT INTO entries VALUES (? , ?);", (entry_content, entry_date)
        )


def get_entries():

    cursor = connection.execute("SELECT * FROM entries;")
    return cursor

    # cursor = connection.cursor()
    # cursor.execute("SELECT * FROM entries;")
