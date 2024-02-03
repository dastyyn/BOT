import sqlite3
from pathlib import Path

def init_db():
    global db, cursor
    db = sqlite3.connect(Path(__file__).parent.parent / 'db.sqlite3')
    cursor = db.cursor()

def create_tables():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS anime (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            autor TEXT,
            duration INTEGER
        );
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS genre (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT
        );
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS anime_genre (
            anime_id INTEGER,
            genre_id INTEGER,
            FOREIGN KEY (anime_id) REFERENCES anime (id),
            FOREIGN KEY (genre_id) REFERENCES genre (id),
            PRIMARY KEY (anime_id, genre_id)
        );
    """)
    cursor.connection.commit()


def populate_db():
    try:

        anime_data = [
            ("Naruto", "Masashi Kishimoto", 220),
            ("One Piece", "Eiichiro Oda", 1091),
            ("Bleach", "Tite Kubo", 366),
            ("Attack on Titan", "Hajime Isayama", 75),
            ("Fullmetal Alchemist", "Hiromu Arakawa", 51),
            ("Monster", "Naoki Urasawa", 75),
            ("Kakegurui", "Homura Kawamoto", 24),
            ("Death Note", "Takeshi Obata", 37),
            ("My Senpai is Annoying", "Shiro Manta", 12),
            ("Hotarubi no Mori e", "Yuki Midorikawa", 1),
            ("Your Name", "Makoto Shinkai", 1),
            ("Kamisama Hajimemashita", "Julietta Suzuki", 25),
            ("Overlord", "Kugane Maruyama", 39),
            ("No Game No Life", "Yuu Kamiya", 12),
            ("Re:Zero", "Tappei Nagatsuki", 50),
            ("The Rising of the Shield Hero", "Aneko Yusagi", 25)
        ]
        genre_data = [
            ("Detective",),
            ("Shonen",),
            ("Romance",),
            ("Isekai",)
        ]
        anime_genre_data = [
            (1, 2),  # Naruto is Shonen
            (2, 2), # One Piece is Shonen
            (3, 2), # Bleach is Shonen
            (4, 2), # Attack on Titan is Shonen
            (5, 2), # Fullmetal Alchemist is Shonen
            (6, 1), # Monster is Detective
            (7, 1), # Kakegurui is Detective
            (8, 1), # Death Note is Detective
            (9, 3), # My Senpai is Annoying is Romance
            (10, 3), # Hotarubi no Mori e is Romance
            (11, 3), # Your Name is Romance
            (12, 3), # Kamisama Hajimemashita is Romance
            (13, 4), # Overlord is Isekai
            (14, 4), # No Game No Life is Isekai
            (15, 4), # Re:Zero is Isekai
            (16, 4) # The Rising of the Shield Hero is Isekai
        ]

        cursor.executemany("INSERT INTO anime (name, autor, duration) VALUES (?, ?, ?)", anime_data)
        cursor.executemany("INSERT INTO genre (name) VALUES (?)", genre_data)
        cursor.executemany("""
            INSERT INTO anime_genre (anime_id, genre_id) VALUES (?, ?)
            ON CONFLICT(anime_id, genre_id) DO NOTHING
        """, anime_genre_data)

        cursor.connection.commit()
    except Exception as e:
        print(f"Error inserting data: {e}")


def close_db():
    cursor.connection.close()


def get_anime_by_genre_name(genre_name: str):
    cursor.execute("""
        SELECT anime.name FROM anime
        JOIN anime_genre ON anime.id = anime_genre.anime_id
        JOIN genre ON anime_genre.genre_id = genre.id
        WHERE genre.name = ?
    """, (genre_name,))
    return cursor.fetchall()


if __name__ == "__main__":
    init_db()
    create_tables()
    populate_db()
    close_db()