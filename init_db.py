from database.session import engine, Base
from database import models

def init_db() -> None:
    print("Инициализация базы данных...")
    Base.metadata.create_all(bind = engine)
    print("Готово. Таблицы созданы (или уже существовали).")

if __name__ == "__main__":
    init_db()