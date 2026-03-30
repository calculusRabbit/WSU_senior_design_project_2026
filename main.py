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
                "event_name": "Hackathon",
                "event_date": "2026-03-20",
                "event_time": "10:00 AM",
                "event_location": "Student Center",
                "event_description": "A coding competition for students"
            },
            {
                "event_id": 2,
                "event_name": "Career Fair",
                "event_date": "2026-03-25",
                "event_time": "1:00 PM",
                "event_location": "Main Hall",
                "event_description": "Meet employers and explore job opportunities"
            }
        ]
    }