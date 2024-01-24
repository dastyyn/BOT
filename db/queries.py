import sqlite3
from pathlib import Path


def init_db():
    global db, cursor
    db = sqlite3.connect(Path(__file__).parent / 'db.sqlite')
    cursor = db.cursor()


def create_tables():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS anime (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            genre TEXT,
            duration INTEGER
        );
    """)
    db.commit()

# Заполнение базы данных anime
def populate_db():
    cursor.execute("""
        INSERT INTO anime (name, genre, duration) VALUES
            ("Deth Note", "Detective", 37),
            ("Naruto", "Senen", 720),
            ("One Piece", "Senen", 1000),
            ("Bleach", "Senen", 366),
            ("My Senpai is annoying", "Romance", 12),
            ("Re:Zero", "Isekai", 50)
    """)
    db.commit()


def get_anime_by_genre(genre):
    cursor.execute("""
        SELECT DISTINCT name FROM anime WHERE genre = ?;
    """, (genre,))
    return cursor.fetchall()


if __name__ == "__main__":
    init_db()
    create_tables()
    populate_db()

