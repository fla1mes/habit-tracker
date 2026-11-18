import flet as ft
import theme

def build_login_view(page: ft.Page, on_login_success, on_go_to_register):
    login_field = ft.TextField(
        label = "Логин",
        prefix_icon = ft.Icons.PERSON,
        width = theme.INPUT_WIDTH,
        height = theme.INPUT_HEIGHT,
        bgcolor = theme.INPUT_BG,
        border_color= theme.BORDER,
        border_radius= theme.INPUT_RADIUS,
        border_width = theme.INPUT_BORDER_WIDTH,
        color= theme.TEXT,
        label_style = ft.TextStyle(color = theme.TEXT_SECONDARY),
    )

    password_field = ft.TextField(
        label = "Пароль",
        password = True,
        can_reveal_password=True,
        prefix_icon=ft.Icons.LOCK,
        width=theme.INPUT_WIDTH,
        height = theme.INPUT_HEIGHT,
        bgcolor=theme.INPUT_BG,
        border_color=theme.BORDER,
        border_radius=theme.INPUT_RADIUS,
        border_width=theme.INPUT_BORDER_WIDTH,
        color=theme.TEXT,
        label_style=ft.TextStyle(color=theme.TEXT_SECONDARY),
    )

    def handle_login_click(e):
        if not login_field.value or not password_field.value:
            snack = ft.SnackBar(
                content = ft.Text("Заполните логин и пароль!", color=ft.Colors.WHITE),
                bgcolor = theme.DANGER,
            )
            page.overlay.append(snack)
            snack.open=True
            page.update()
            return

        on_login_success()

    login_button = ft.Button(
        content = "Войти",
        width = theme.BUTTON_WIDTH,
        height = theme.BUTTON_HEIGHT,

        color = ft.Colors.WHITE,
        on_click = handle_login_click,
        style = ft.ButtonStyle(bgcolor = theme.PRIMARY,shape=ft.RoundedRectangleBorder(radius=theme.BUTTON_RADIUS),)
    )

    register_row = ft.Row(
        [
            ft.Text(
                "Нет аккаунта?",
                color=theme.TEXT_SECONDARY,
                size=theme.TEXT_SIZE,
            ),
            ft.TextButton(
                content="Зарегистрироваться",
                style=ft.ButtonStyle(
                    color=theme.PRIMARY,
                    padding=0,
                ),
                on_click=lambda e: on_go_to_register(),
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=0,
    )

    return ft.Container(
        content=ft.Column(
            [
                ft.Icon(ft.Icons.CHECK_CIRCLE_OUTLINE, size=60, color=theme.PRIMARY),
                ft.Text("Habit Tracker", size=theme.TITLE_SIZE, weight=ft.FontWeight.BOLD, color=theme.TEXT),
                ft.Text("Отслеживай свои привычки", size=theme.SUBTITLE_SIZE, color=theme.TEXT_SECONDARY),

                ft.Divider(height=20, color=ft.Colors.TRANSPARENT),

                login_field,
                password_field,

                ft.Divider(height=10, color=ft.Colors.TRANSPARENT),

                login_button,

                ft.Divider(height=5, color=ft.Colors.TRANSPARENT),

                register_row,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        expand=True,
        bgcolor=theme.BACKGROUND,
        padding=20,
    )