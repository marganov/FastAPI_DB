import asyncio
import asyncpg
from pathlib import Path
from db.settings import settings


async def create_all_tables():
    """Создает все таблицы в одной сессии"""
    conn = None
    try:
        conn = await asyncpg.connect(settings.DB_URL)
        print("✅ Подключение к базе данных установлено")
        
        # Создаем таблицу items
        items_sql_path = Path(__file__).parent / "migrations" / "001_create_table_items.sql"
        with open(items_sql_path, "r", encoding='utf-8') as f:
            items_script = f.read()
        await conn.execute(items_script)
        print("✅ Таблица items создана")
        
        # Создаем таблицу users
        users_sql_path = Path(__file__).parent / "migrations" / "002_create_table_users.sql"
        with open(users_sql_path, "r", encoding='utf-8') as f:
            users_script = f.read()
        await conn.execute(users_script)
        print("✅ Таблица users создана")
        
        print("🎉 Все таблицы успешно созданы!")
        
    except Exception as e:
        print(f"❌ Ошибка: {e}")
    finally:
        if conn:
            await conn.close()
        print("✅ Подключение закрыто")


if __name__ == "__main__":
    asyncio.run(create_all_tables())