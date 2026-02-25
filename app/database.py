import asyncpg
from fastapi import Request
from .config import DB_CONFIG

async def create_pool() -> asyncpg.Pool:
    return await asyncpg.create_pool(
        **DB_CONFIG,
        min_size=1,
        max_size=10
    )

async def create_tables(pool: asyncpg.Pool):
    async with pool.acquire() as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id       SERIAL PRIMARY KEY,
                username VARCHAR(50) UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        """)

async def get_db(request: Request):
    async with request.app.state.db.acquire() as db:
        yield db