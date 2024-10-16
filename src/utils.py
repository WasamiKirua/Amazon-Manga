import sqlite3

db_name = '/app/data/amazon-manga.db'

def create_sqlite_database():
    """ create a database connection to an SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_name)
    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def create_main_tables():
    conn = None
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()

        # Creating manga table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS manga (
                    id INTEGER PRIMARY KEY,
                    title TEXT,
                    url TEXT,
                    price NUMERIC,
                    availability TEXT,
                    rating NUMERIC,
                    trama TEXT,
                    cover BLOB
            )''')
        conn.commit()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS urls (
                    id INTEGER PRIMARY KEY,
                    url TEXT
            )''')
        conn.commit()

    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def add_url(url: str):
    conn = None
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO urls (url) VALUES (?)", (url,))
        conn.commit()
    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

