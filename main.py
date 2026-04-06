from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Smart Campus Backend is running"}

@app.get("/events")
def get_events():
    return {
        "events": [
            {
                "event_id": 1,
                "event_name": "C++ Competition",
                "event_date": "2026-03-20",
                "event_time": "10:00 AM",
                "event_location": "Rhatigan Student Center",
                "event_description": "A coding competition for students"
            },
            {
                "event_id": 2,
                "event_name": "Career Fair",
                "event_date": "2026-03-25",
                "event_time": "1:00 PM",
                "event_location": "John Bardo Center",
                "event_description": "Meet employers and explore job opportunities"
            }
        ]
    }

@app.get("/dining")
def get_dining():
    return {
        "dining": [
            {
                "dining_id": 1,
                "dining_name": "Chick Fil-A",
                "opening_time": "7:00 AM",
                "closing_time": "10:00 PM",
                "dining_location": "Rathigan Student Center",
                "dining_status": "Open"
            },
            {
                "dining_id": 2,
                "dining_name": "Panda Express",
                "opening_time": "7:00 AM",
                "closing_time": "10:00 PM",
                "dining_location": "Rathigan Student Center",
                "dining_status": "Open"
            }
        ]
    }

@app.get("/courses")
def get_courses():
    return {
        "courses": [
            {
                "course_id": 101,
                "course_code": "CS 598",
                "course_name": "Senior Design Project",
                "course_department": "Computer Science",
                "course_description": "Capstone project course for senior students",
                "course_credits": 3
            },
            {
                "course_id": 102,
                "course_code": "CS 770",
                "course_name": "Machine Learning",
                "course_department": "Computer Science",
                "course_description": "Introduction to machine learning concepts and models",
                "course_credits": 3
            }
        ]
    }

@app.get("/professors")
def get_professors():
    return {
        "professors": [
            {
                "professor_id": 101,
                "professor_name": "Professor Cody.AI",
                "professor_department": "Computer Science",
                "professor_email": "codyai@wsu.edu",
                "office_location": "Room 209",
                "professor_rating": 4.7
            },
            {
                "professor_id": 102,
                "professor_name": "Professor Thomas.AI",
                "professor_department": "Computer Science",
                "professor_email": "thomasai@wsu.edu",
                "office_location": "Room 201",
                "professor_rating": 4.5
            }
        ]
    }