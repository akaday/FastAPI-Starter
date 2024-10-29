# app/models.py
from sqlalchemy import Table, Column, Integer, String, ForeignKey
from .database import metadata

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("email", String)
)

posts = Table(
    "posts",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String),
    Column("content", String),
    Column("owner_id", Integer, ForeignKey("users.id"))
)
