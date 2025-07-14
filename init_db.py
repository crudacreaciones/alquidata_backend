# init_db.py
import asyncio
import asyncpg
from config import settings

async def init():
    conn = await asyncpg.connect(dsn=settings.DATABASE_URL)
    with open("schema.sql", "r") as f:
        await conn.execute(f.read())
    await conn.close()
    print("✅ Base de datos inicializada.")

if __name__ == "__main__":
    asyncio.run(init())

