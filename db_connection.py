from fastapi import FastAPI
from contextlib import contextmanager
from pydantic import BaseModel

app = FastAPI()

class SessionLocal:
    def start(self):
        print("Session started")
        return self

    def close(self):
        print("Session closed")

class User(BaseModel):
    name: str
    age: int

@contextmanager
def get_db():
    db = SessionLocal()
    try:
        db.start()
        yield db
    finally:
        db.close()

@app.post("/save/")
def save_data(user: User):
    with get_db() as db:
        print(f"Saving user: {user}")
        return {"status": "Data Saved successfully!"}
