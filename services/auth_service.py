from sqlalchemy.orm import Session
from database.models import User
from services.security import get_password_hash, verify_password


class UserAlreadyExistsError(Exception):
    """Вызывается, если логин уже занят."""
    pass


class InvalidCredentialsError(Exception):
    """Вызывается, если логин или пароль неверные."""
    pass



def register_user(db: Session, username: str, password: str) -> User:
    """
    Регистрирует нового пользователя.
    
    :param db: Сессия SQLAlchemy
    :param username: Логин
    :param password: Чистый пароль
    :return: Объект User
    :raises UserAlreadyExistsError: если такой логин уже есть
    """
    # 1. Проверяем, нет ли уже такого пользователя
    existing_user = db.query(User).filter(User.username == username).first()
    if existing_user:
        raise UserAlreadyExistsError(f"Пользователь с логином '{username}' уже существует.")

    # 2. Хешируем пароль
    hashed_pwd = get_password_hash(password)

    # 3. Создаем и сохраняем пользователя
    new_user = User(username=username, password_hash=hashed_pwd)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)  # Обновляем объект, чтобы получить id из БД

    return new_user


def authenticate_user(db: Session, username: str, password: str) -> User:
    """
    Проверяет логин и пароль.
    
    :param db: Сессия SQLAlchemy
    :param username: Логин
    :param password: Чистый пароль
    :return: Объект User, если пароль верный
    :raises InvalidCredentialsError: если логин не найден или пароль неверный
    """
    # 1. Ищем пользователя по логину
    user = db.query(User).filter(User.username == username).first()
    
    # 2. Если пользователя нет — ошибка
    if not user:
        raise InvalidCredentialsError("Неверный логин или пароль.")

    # 3. Проверяем пароль
    if not verify_password(password, user.password_hash):
        raise InvalidCredentialsError("Неверный логин или пароль.")

    
    return user