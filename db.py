# app/db.py
import asyncpg
from config import settings

async def get_connection():
    return await asyncpg.connect(dsn=settings.DATABASE_URL)

