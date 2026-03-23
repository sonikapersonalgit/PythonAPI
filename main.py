from fastapi import FastAPI
app=FastAPI()

users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
    {"id": 3, "name": "Charlie"}
]

@app.get("/")
def home():
    return{"message":"My name is Sonika"}

@app.get("/users")
def get_users():
    return{"users":users}
