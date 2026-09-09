# requires: psycopg, bcrypt
# populates postgres database (according to schema in sca_database_v0.2.0.sql) with dummy data

# run command: python <this_script_name> <path_to_db> 

import os
import sys
import psycopg
import random
from datetime import datetime, timedelta
import bcrypt

seed = random.Random(67)

# same password for all dummy accounts
dummy_password = "password123"
#only hashing once and using this result for efficiency
salt = bcrypt.gensalt()
hash = bcrypt.hashpw(dummy_password, salt)

#wipes any existing dummy data from all tables for a fresh re-population
def erase_data(cur):
    cur.execute("""
        TRUNCATE Schools, Users, Departments, Locations, Dining, 
        Courses, Sessions, Offerings, Students, Deadlines, Instructors, 
        Reviews_generic, Review_votes, Review_replies, Reviews_educational, 
        Reviews_dining, Dining_items, Reviews_resources, Authentications, Notifications,
        Groups, Memberships, Registrations, Event_responses, Scraped_information, 
        Attendance
        RESTART IDENTITY CASCADE
    """)

# runs an insert operation and returns the serials created
def insert(cur, query, params):
    cur.execute(query, params)
    return cur.fetchone()[0]

#inserts dummy data into all tables
def insert_all(curr):
    
    school_ids = []
    for i in range(10):
        school_id = insert(cur, "INSERT INTO Schools (school_name) VALUES (%s) RETURNING school_id",
        (f"{random.choice("University", "College")} of Test {i+1}",)
        )
    school_ids.append(school_id)


    department_ids = []
    i = 1
    for school_id in school_ids:
        dept_id = insert(cur, "INSERT INTO Departments (school_id, department_name, department_code) "
        "VALUES (%s, %s, %s) RETURNING department_id", (school_id, 
        f"Test {random.choice("Department", "School")} {i}", f"TEST{i}")
        )
        i+=1
        department_ids.append((dept_id, school_id))


    location_ids = []
    for school_id in school_ids:
        location_id = insert(cur, "INSERT INTO LOCATIONS (school_id, address_street, "
        "address_room, city, state_code, zipcode, on_campus, location_status, "
        "open_hours) "
        "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s) RETURNING location_id",
        (school_id, f"{random.randint(1,5000)} Test {random.choice("St","Rd","Ln","Circle","Dr")}",
        f"{random.choice("room","Rm","suite")} {random.randint(1,400)}", 
        f"Test City {random.randint(1,10)}", f"{10000+random.randint(1,9999)}", True, "active",
        "[{“days”: [0,6], “times”: []}, {“days”: [1,2,3,4,5], “times”: [[“09:00”, ”17:00”]]}")
        )
        location_ids.append(location_id)
    
    for i in range(5):
        insert(cur, "INSERT INTO Users (username, account_type, hashed_password) "
        "VALUES (%s,%s,%s) RETURNING username", (f"test_admin{i}","admin",hash))
        insert(cur, "INSERT INTO Users (username, account_type, hashed_password) "
        "VALUES (%s,%s,%s) RETURNING username", (f"test_student{i}","student",hash))

    session_ids = []
    for school_id in school_ids:
        session_id = insert(cur, "INSERT INTO Sessions (school_id, session_name, academic_year, "
        "session_start, session_end) VALUES (%s,%s,%s,%s,%s) RETURNING session_id",
        (school_id, f"{random.choice("Fall","Spring")} 2026", 2026, "2026-08-17", "2026-12-03"))
        
        session_ids.append((session_id, school_id))

    
    course_ids = []
    for (dept_id, school_id) in department_ids:
        course_id = insert(cur, "INSERT INTO Courses (department_id, course_code, course_number, "
        "course_name, course_description, course_credits) "
        "VALUES (%s,%s,%s,%s,%s,%s) RETURNING course_id",
        (department_id, "TEST", f"{randint(100,900)}", "Test Course", "Test course description.", 3.0))
        course_ids.append((course_id, department_id, school_id))

    
    #TODO: insertions to remaining tables
    


def main():
    if len(sys.argv) != 2:
        sys.exit("Incorrect number of arguments; provide path to database file and optionally number of students.")
    path_to_db = sys.argv[1]       
    
    try:
        with psycopg.connect("dbname=test user=postgres") as conn:
            with conn.cursor() as cur:
                erase_data(cur)
                
                insert_all(curr)
                print("Fresh dummy data inserted into database")
                conn.commit()
                
    except Exception as ex:
        sys.exit(f"Failed to open/write to database: {ex}")