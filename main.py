from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

notes = {}

class Note(BaseModel):
    title: str
    content: str

@app.get("/")
def home():
    return {"message": "Notebook API"}

@app.post("/notes")
def create_note(note: Note):
    notes[note.title] = note.content
    return {"message": "Note added"}

@app.get("/notes")
def get_notes():
    return notes

@app.get("/notes/{title}")
def get_note(title: str):
    return {
        "title": title,
        "content": notes.get(title, "Not Found")
    }

@app.delete("/notes/{title}")
def delete_note(title: str):
    notes.pop(title, None)
    return {"message": "Deleted"}
