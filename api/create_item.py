from fastapi import FastAPI, Depends, HTTPException
from db.connector import get_db_connection
from db.models.item_model import ItemCreate
import asyncpg

app = FastAPI(description="simple ruchka")

@app.post("/items_test")
async def create_item(
    item: ItemCreate,
    db: asyncpg.Connection = Depends(get_db_connection)
):
    try:
        row = await db.fetchrow("INSERT INTO items(name) VALUES($1) RETURNING id, name, created_at", item.name)

        return dict(row)  # type: ignore
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))