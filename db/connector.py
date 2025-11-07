import asyncpg
from .settings import settings

async def get_db_connection():
    conn = await asyncpg.connect(settings.DB_URL)
    try:
        yield conn
    finally:
        await conn.close()