from fastapi import FastAPI
from .database import database, engine, metadata
from .models import users

metadata.create_all(engine)
app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI Starter by Akaday!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.post("/users/")
async def create_user(name: str, email: str):
    query = users.insert().values(name=name, email=email)
    await database.execute(query)
    return {"name": name, "email": email}
