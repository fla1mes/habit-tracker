from database.session import SessionLocal
from services.auth_service import (
    register_user, 
    authenticate_user, 
    UserAlreadyExistsError, 
    InvalidCredentialsError
)

def run_test():
    db = SessionLocal()
    
    test_login = "test_user"
    test_pass = "super_secret_123"

    print("--- 1. Тест регистрации ---")
    try:
        user = register_user(db, test_login, test_pass)
        print(f"✅ Успех! Создан пользователь: {user.username} (id={user.id})")
    except UserAlreadyExistsError as e:
        print(f"⚠️ Пользователь уже существует: {e}")
    except Exception as e:
        print(f"❌ Неизвестная ошибка: {e}")

    print("\n--- 2. Тест входа (верный пароль) ---")
    try:
        user = authenticate_user(db, test_login, test_pass)
        print(f"✅ Успех! Вход выполнен: {user.username}")
    except InvalidCredentialsError as e:
        print(f"❌ Ошибка входа: {e}")

    print("\n--- 3. Тест входа (неверный пароль) ---")
    try:
        user = authenticate_user(db, test_login, "wrong_password")
        print(f"❌ ОШИБКА ТЕСТА: Пустило с неверным паролем!")
    except InvalidCredentialsError as e:
        print(f"✅ Ожидаемая ошибка: {e}")

    print("\n--- 4. Тест входа (несуществующий логин) ---")
    try:
        user = authenticate_user(db, "ghost_user", "any_password")
        print(f"❌ ОШИБКА ТЕСТА: Пустило с несуществующим логином!")
    except InvalidCredentialsError as e:
        print(f"✅ Ожидаемая ошибка: {e}")

    # Закрываем сессию
    db.close()
    print("\nТестирование завершено.")

if __name__ == "__main__":
    run_test()