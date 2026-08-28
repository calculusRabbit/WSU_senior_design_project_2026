import sqlite3

DATABASE_NAME = "smart_campus.db"


def get_connection():
    connection = sqlite3.connect(DATABASE_NAME)
    connection.row_factory = sqlite3.Row
    return connection


def create_tables():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS events (
            event_id INTEGER PRIMARY KEY,
            event_name TEXT NOT NULL,
            event_date TEXT NOT NULL,
            event_time TEXT NOT NULL,
            event_location TEXT NOT NULL,
            event_description TEXT,
            event_category TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS student_interests (
            interest_id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER NOT NULL,
            interest TEXT NOT NULL
        )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS deadlines (
        deadline_id INTEGER PRIMARY KEY,
        deadline_title TEXT NOT NULL,
        deadline_date TEXT NOT NULL,
        deadline_description TEXT
    )
""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS courses (
        id INTEGER PRIMARY KEY,
        code TEXT NOT NULL,
        name TEXT NOT NULL,
        time TEXT NOT NULL,
        room TEXT NOT NULL,
        professor TEXT NOT NULL,
        department TEXT NOT NULL,
        description TEXT,
        credits INTEGER NOT NULL
    )
""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS professors (
        professor_id INTEGER PRIMARY KEY,
        professor_name TEXT NOT NULL,
        professor_department TEXT NOT NULL,
        professor_email TEXT,
        office_location TEXT,
        professor_rating REAL
    )
""")

    connection.commit()
    connection.close()

def insert_sample_events():
    connection = get_connection()
    cursor = connection.cursor()

    events = [
        (
            1,
            "C++ Competition",
            "2026-09-20",
            "10:00 AM",
            "Rhatigan Student Center",
            "A coding competition for students",
            "coding"
        ),
        (
            2,
            "Career Fair",
            "2026-09-25",
            "1:00 PM",
            "John Bardo Center",
            "Meet employers and explore job opportunities",
            "career"
        )
    ]

    cursor.executemany("""
        INSERT OR REPLACE INTO events (
            event_id,
            event_name,
            event_date,
            event_time,
            event_location,
            event_description,
            event_category
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, events)

    connection.commit()
    connection.close()

def get_events_from_database():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM events")
    rows = cursor.fetchall()

    events = [dict(row) for row in rows]

    connection.close()
    return events

def save_student_interests(student_id: int, interests: list[str]):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM student_interests WHERE student_id = ?",
        (student_id,)
    )

    for interest in interests:
        cursor.execute(
            """
            INSERT INTO student_interests (student_id, interest)
            VALUES (?, ?)
            """,
            (student_id, interest.lower().strip())
        )

    connection.commit()
    connection.close()

def get_student_interests(student_id: int):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT interest
        FROM student_interests
        WHERE student_id = ?
        """,
        (student_id,)
    )

    rows = cursor.fetchall()

    interests = [row["interest"] for row in rows]

    connection.close()
    return interests

def insert_sample_deadlines():
    connection = get_connection()
    cursor = connection.cursor()

    deadlines = [
        (
            1,
            "Course Registration Deadline",
            "2026-10-15",
            "Last day to register for Spring classes"
        ),
        (
            2,
            "Add/Drop Deadline",
            "2026-09-10",
            "Last day to add or drop a course without penalty"
        )
    ]

    cursor.executemany("""
        INSERT OR REPLACE INTO deadlines (
            deadline_id,
            deadline_title,
            deadline_date,
            deadline_description
        )
        VALUES (?, ?, ?, ?)
    """, deadlines)

    connection.commit()
    connection.close()

def get_deadlines_from_database():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM deadlines")
    rows = cursor.fetchall()

    deadlines = [dict(row) for row in rows]

    connection.close()
    return deadlines

def insert_sample_courses():
    connection = get_connection()
    cursor = connection.cursor()

    courses = [
        (
            1,
            "CS 560",
            "Machine Learning",
            "TR 2:00-3:15 PM",
            "Jabara 210",
            "Dr. Yang",
            "Computer Science",
            "Introduction to machine learning concepts and models",
            3
        ),
        (
            2,
            "CS 598",
            "Senior Design Project",
            "MW 10:00-11:15 AM",
            "RSC 261",
            "Dr. Smith",
            "Computer Science",
            "Capstone project course for senior students",
            3
        )
    ]

    cursor.executemany("""
        INSERT OR REPLACE INTO courses (
            id,
            code,
            name,
            time,
            room,
            professor,
            department,
            description,
            credits
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, courses)

    connection.commit()
    connection.close()

def get_courses_from_database():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM courses")
    rows = cursor.fetchall()

    courses = [dict(row) for row in rows]

    connection.close()
    return courses

def insert_sample_professors():
    connection = get_connection()
    cursor = connection.cursor()

    professors = [
        (
            101,
            "Professor Cody",
            "Computer Science",
            "cody@wsu.edu",
            "Room 209",
            4.7
        ),
        (
            102,
            "Professor Thomas",
            "Computer Science",
            "thomas@wsu.edu",
            "Room 201",
            4.5
        )
    ]

    cursor.executemany("""
        INSERT OR REPLACE INTO professors (
            professor_id,
            professor_name,
            professor_department,
            professor_email,
            office_location,
            professor_rating
        )
        VALUES (?, ?, ?, ?, ?, ?)
    """, professors)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS dining (
        dining_id INTEGER PRIMARY KEY,
        dining_name TEXT NOT NULL,
        opening_time TEXT NOT NULL,
        closing_time TEXT NOT NULL,
        dining_location TEXT NOT NULL,
        dining_status TEXT NOT NULL
    )
""")

    connection.commit()
    connection.close()

def get_professors_from_database():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM professors")
    rows = cursor.fetchall()

    professors = [dict(row) for row in rows]

    connection.close()
    return professors

def insert_sample_dining():
    connection = get_connection()
    cursor = connection.cursor()

    dining = [
        (
            1,
            "Chick-fil-A",
            "7:00 AM",
            "10:00 PM",
            "Rhatigan Student Center",
            "Open"
        ),
        (
            2,
            "Panda Express",
            "7:00 AM",
            "10:00 PM",
            "Rhatigan Student Center",
            "Open"
        )
    ]

    cursor.executemany("""
        INSERT OR REPLACE INTO dining (
            dining_id,
            dining_name,
            opening_time,
            closing_time,
            dining_location,
            dining_status
        )
        VALUES (?, ?, ?, ?, ?, ?)
    """, dining)

    connection.commit()
    connection.close()

def get_dining_from_database():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM dining")
    rows = cursor.fetchall()

    dining = [dict(row) for row in rows]

    connection.close()
    return dining

if __name__ == "__main__":
    create_tables()
    insert_sample_events()
    insert_sample_deadlines()
    insert_sample_courses()
    insert_sample_professors()
    insert_sample_dining()
    print("Smart Campus database initialized successfully.")