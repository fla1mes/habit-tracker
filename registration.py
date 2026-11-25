from database.session import SessionLocal
from services.auth_service import register_user, UserAlreadyExistsError
import flet as ft
import theme

def main(page: ft.Page):
    page.title = "Habit Tracker"
    page.bgcolor = theme.BACKGROUND
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.padding = 20

    login_field = ft.TextField(
        label = "Логин",
        width = theme.INPUT_WIDTH,
        height = theme.INPUT_HEIGHT,
        bgcolor = theme.INPUT_BG,
        border = ft.OutlineInputBorder(
            border_radius = theme.INPUT_RADIUS,
            side = ft.BorderSide(
                color = theme.BORDER,
                width = theme.INPUT_BORDER_WIDTH
            )
        ),
        text_size = theme.TEXT_SIZE
    )

    password_field = ft.TextField(
        label = "Пароль",
        password = True,
        can_reveal_password = True,
        width = theme.INPUT_WIDTH,
        height = theme.INPUT_HEIGHT,
        bgcolor = theme.INPUT_BG,
        border=ft.OutlineInputBorder(
            border_radius=theme.INPUT_RADIUS,
            side=ft.BorderSide(
                color=theme.BORDER,
                width=theme.INPUT_BORDER_WIDTH
            )
        ),
        text_size = theme.TEXT_SIZE
    )

    confirm_password_field = ft.TextField(
        label = "Повторите пароль",
        password=True,
        can_reveal_password=True,
        width=theme.INPUT_WIDTH,
        height=theme.INPUT_HEIGHT,
        bgcolor=theme.INPUT_BG,
        border=ft.OutlineInputBorder(
            border_radius=theme.INPUT_RADIUS,
            side=ft.BorderSide(
                color=theme.BORDER,
                width=theme.INPUT_BORDER_WIDTH
            )
        ),
        text_size=theme.TEXT_SIZE
    )

    message = ft.Text(
        size = theme.TEXT_SIZE,
        text_align = ft.TextAlign.CENTER
    )

    def register(e):
        username = login_field.value.strip()
        password = password_field.value
        confirm_password = confirm_password_field.value

        if (
            not username
            or not password
            or not confirm_password
        ):
            message.value = "Заполните все поля!"
            message.color = theme.DANGER

        elif password != confirm_password:
             message.value = "Пароли не совпадают!"
             message.color = theme.DANGER

        else:
            db = SessionLocal()

            try:
                user = register_user(db, username, password)

                message.value = "Регистрация прошла успешно!"
                message.color = theme.SUCCESS

            except UserAlreadyExistsError:
                message.value = "Такой логин уже занят!"
                message.color = theme.DANGER

            except Exception as error:
                message.value = "Ошибка регистрации!"
                message.color = theme.DANGER
                print(error)

            finally:
                db.close()

        page.update()

    register_button = ft.Button(
        content="Зарегистрироваться",
        width=theme.BUTTON_WIDTH,
        height=theme.BUTTON_HEIGHT,
        bgcolor=theme.PRIMARY,
        color=theme.BACKGROUND,
        on_click=register
    )

    login_link = ft.TextButton(
        content="Войти",
        on_click=lambda e: print(
            "Переход на экран входа"
        )
    )


    registration_card = ft.Container(
        content = ft.Column(
            controls = [
                ft.Text(
                    "Создать аккаунт",
                    size = theme.TITLE_SIZE,
                    weight = ft.FontWeight.BOLD,
                    color = theme.TEXT
                ),

                ft.Text(
                    "Заполните данные для регистрации",
                    size = theme.SUBTITLE_SIZE,
                    color = theme.TEXT_SECONDARY
                ),

                login_field,
                password_field,
                confirm_password_field,

                register_button,
                message,

                ft.Row(
                    controls = [
                        ft.Text(
                            "Уже есть аккаунт?",
                            size = theme.TEXT_SIZE,
                            color = theme.TEXT_SECONDARY
                        ),
                        login_link
                    ],
                    alignment = ft.MainAxisAlignment.CENTER
                )
            ],
            spacing = 15,
            horizontal_alignment = ft.CrossAxisAlignment.CENTER
        ),
        width = 400,
        padding = 30,
        bgcolor = theme.BACKGROUND,
        border = ft.Border.all(1, theme.BORDER),
        border_radius = 20
    )

    page.add(
        registration_card
    )

ft.run(main)