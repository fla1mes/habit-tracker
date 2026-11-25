import flet as ft
import theme

def build_login_view(page: ft.Page, on_login_success, on_go_to_register):
    login_field = ft.TextField(
        label = "Логин",
        prefix_icon = ft.Icons.PERSON,
        width = theme.INPUT_WIDTH,
        height = theme.INPUT_HEIGHT,
        bgcolor = theme.INPUT_BG,
        border = ft.OutlineInputBorder(
            border_radius= theme.INPUT_RADIUS,
            side = ft.BorderSide(
                color = theme.BORDER,
                width = theme.INPUT_BORDER_WIDTH)),
        text_size = theme.TEXT_SIZE,
    )

    password_field = ft.TextField(
        label = "Пароль",
        password = True,
        can_reveal_password=True,
        prefix_icon=ft.Icons.LOCK,
        width=theme.INPUT_WIDTH,
        height = theme.INPUT_HEIGHT,
        bgcolor=theme.INPUT_BG,
        border=ft.OutlineInputBorder(
            border_radius=theme.INPUT_RADIUS,
            side=ft.BorderSide(
                color=theme.BORDER,
                width=theme.INPUT_BORDER_WIDTH)),
        text_size=theme.TEXT_SIZE,
    )
    message = ft.Text(
        size = theme.TEXT_SIZE,
        text_align = ft.TextAlign.CENTER,
    )

    def handle_login_click(e):
        if not login_field.value or not password_field.value:
            message.value = "Заполните логин и пароль!"
            message.color = theme.DANGER
        else:
            message.value=""
            on_login_success()
        page.update()

    login_button = ft.Button(
        content = "Войти",
        width = theme.BUTTON_WIDTH,
        height = theme.BUTTON_HEIGHT,
        bgcolor = theme.PRIMARY,
        color=theme.BACKGROUND,
        on_click = handle_login_click,
        style = ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=theme.BUTTON_RADIUS),)
    )

    register_link=ft.TextButton(
        content = "Зарегистрироваться",
        on_click=lambda e: on_go_to_register(),
        style = ft.ButtonStyle(
            color = theme.PRIMARY,
            padding = ft.Padding.symmetric(horizontal=5,vertical = 0),
        ),
    )

    login_card = ft.Container(
        content = ft.Column(
            controls = [
                ft.Text(
                    "Вход в аккаунт",
                    size=theme.TITLE_SIZE,
                    weight=ft.FontWeight.BOLD,
                    color = theme.TEXT,
                ),
                ft.Text(
                    "Введите логин и пароль",
                    size=theme.SUBTITLE_SIZE,
                    color=theme.TEXT_SECONDARY,
                ),
                login_field,
                password_field,

                login_button,

                message,

                ft.Row(
                    controls =[
                        ft.Text(
                            "Нет аккаунта?",
                            size =theme.TEXT_SIZE,
                            color = theme.TEXT_SECONDARY,
                        ),
                        register_link,
                    ],
                    alignment = ft.MainAxisAlignment.CENTER,
                    spacing=5,
                ),
            ],
            spacing=15,
            horizontal_alignment = ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        width =400,
        height = 500,
        padding = 30,
        bgcolor = theme.BACKGROUND,
        border =ft.Border.all(1,theme.BORDER),
        border_radius=20,
    )

    return ft.Container(
        content = login_card,
        expand=True,
        bgcolor=theme.BACKGROUND,
        alignment = ft.Alignment(0,0)
    )