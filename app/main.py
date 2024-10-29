from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from .database import database, engine, metadata
from .models import users, posts
from .schemas import UserCreate, UserRead, PostCreate, PostRead
from .auth import authenticate_user, create_access_token, get_current_user, get_user_by_id

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
async def create_user(user: UserCreate):
    query = users.insert().values(name=user.name, email=user.email, password=user.password)
    await database.execute(query)
    return {"name": user.name, "email": user.email}

@app.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/users/me", response_model=UserRead)
async def read_users_me(current_user: UserRead = Depends(get_current_user)):
    return current_user

@app.post("/posts/", response_model=PostRead)
async def create_post(post: PostCreate):
    query = posts.insert().values(title=post.title, content=post.content, owner_id=post.owner_id)
    post_id = await database.execute(query)
    return {**post.dict(), "id": post_id}

@app.get("/posts/{post_id}", response_model=PostRead)
async def read_post(post_id: int):
    query = posts.select().where(posts.c.id == post_id)
    post = await database.fetch_one(query)
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

@app.get("/users/{user_id}/posts", response_model=List[PostRead])
async def read_user_posts(user_id: int):
    query = posts.select().where(posts.c.owner_id == user_id)
    user_posts = await database.fetch_all(query)
    return user_posts
