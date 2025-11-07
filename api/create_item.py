from fastapi import FastAPI, Depends
from db.connector import get_db_connection
from db.models.item_model import Item
import asyncpg

app = FastAPI(description="simple ruchka")

@app.post("/items_test")
async def create_item(
    item: Item,
    db: asyncpg.Connection = Depends(get_db_connection)
):
    await db.execute(
        '''
        INSERT INTO items(name) VALUES($1)
        ''', item.name
    )
    return {
        "message": "Success"
    }