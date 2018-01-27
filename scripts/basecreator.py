import sqlite3
import os


def basecreator():
    if os.path.isfile("test.db"):
        os.remove('test.db')
    conn = sqlite3.connect("test.db")
    c = conn.cursor()

    for statement in table_creator.split(";"):
        c.execute(statement)

    conn.commit()
    conn.close()


if __name__ == "__main__":
    basecreator()
