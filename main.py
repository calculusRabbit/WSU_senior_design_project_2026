from fastapi import FastAPI

from data import (
    events_data,
    dining_data,
    courses_data,
    professors_data,
    deadlines_data,
)
from models import ChatRequest

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Smart Campus Backend is running"}


@app.get("/events")
def get_events():
    return {"events": events_data()}


@app.get("/dining")
def get_dining():
    return {"dining": dining_data()}


@app.get("/courses")
def get_courses():
    return {"courses": courses_data()}


@app.get("/professors")
def get_professors():
    return {"professors": professors_data()}


@app.get("/deadlines")
def get_deadlines():
    return {"deadlines": deadlines_data()}


@app.post("/chat")
def chat(request: ChatRequest):
    message = request.message.lower()

    event_keywords = ["event", "events", "activity", "activities", "career fair", "competition"]
    dining_keywords = ["dining", "food", "eat", "cafeteria", "restaurant", "hungry"]
    course_keywords = ["course", "courses", "class", "classes", "cs 560", "cs 598"]
    professor_keywords = ["professor", "instructor", "teacher", "who teaches", "dr."]
    deadline_keywords = ["deadline", "deadlines", "registration", "add/drop", "due date"]

    if any(keyword in message for keyword in event_keywords):
        return {
            "intent": "events",
            "reply": "Here are some upcoming campus events.",
            "data": events_data()
        }

    elif any(keyword in message for keyword in dining_keywords):
        return {
            "intent": "dining",
            "reply": "Here are some dining options on campus.",
            "data": dining_data()
        }

    elif any(keyword in message for keyword in course_keywords):
        return {
            "intent": "courses",
            "reply": "Here are some course details.",
            "data": courses_data()
        }

    elif any(keyword in message for keyword in professor_keywords):
        return {
            "intent": "professors",
            "reply": "Here are some professor details.",
            "data": professors_data()
        }

    elif any(keyword in message for keyword in deadline_keywords):
        return {
            "intent": "deadlines",
            "reply": "Here are some important academic deadlines.",
            "data": deadlines_data()
        }

    else:
        return {
            "intent": "unknown",
            "reply": "Sorry, I can currently help with events, dining, courses, professors, and deadlines. Try asking about campus events, food, classes, instructors, or deadlines."
        }