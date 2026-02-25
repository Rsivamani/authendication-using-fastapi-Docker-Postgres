from contextlib import asynccontextmanager
from fastapi import FastAPI
from dotenv import load_dotenv
from app.users.router import router as users_router

load_dotenv()

from .database import create_pool, create_tables

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.db = await create_pool()  
    await create_tables(app.state.db)   
    yield                               
    await app.state.db.close()         

app = FastAPI(lifespan=lifespan)

app.include_router(users_router)