import sqlite3
from settings import DATABASE_NAME


def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn

def create_tables():
    tables =[
        """CREATE TABLE IF NOT EXISTS "taquitos" (
	        "id"	INTEGER NOT NULL UNIQUE,
	        "name"	TEXT NOT NULL,
	        "rate"	INTEGER NOT NULL DEFAULT 5,
	        "image"	TEXT UNIQUE,
	        PRIMARY KEY("id" AUTOINCREMENT)
            )"""
    ]
    db = get_db()
    cursor = db.cursor()
    for table in tables:
        cursor.execute(table)