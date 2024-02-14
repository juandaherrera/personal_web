import reflex as rx

from personal_web.styles.colors import Color
from personal_web.styles.styles import Size


def menu() -> rx.Component:
    return rx.menu(
        rx.menu_button(
            rx.icon(
                tag="hamburger",
                font_size=Size.DEFAULT_BIG.value,
            ),
            transition="color 0.2s ease",
            _hover={
                "color": Color.SECONDARY.value,
            },
        ),
        rx.menu_list(
            _menu_item("Acerca de mí 👨🏻‍💻", "#about_me"),
            _menu_item("Experiencia 💼", "#experience"),
            _menu_item("Proyectos 💻", "#projects"),
            rx.menu_divider(),
            _menu_item("Educación 📖", "#education"),
            _menu_item("Certificaciones 📃", "#certifications"),
            _menu_item("Cursos 📝", "#courses"),
            background=Color.CONTENT.value,
            border_color=Color.BACKGROUND.value,
        ),
    )


# TO_DO revisar emojis a la derecha del todo
def _menu_item(text: str, url: str, is_external: bool = False) -> rx.Component:
    return rx.menu_item(
        rx.link(rx.text(text), href=url, is_external=is_external),
        background="transparent",
        transition="color 0.2s ease",
        _hover={"color": Color.SECONDARY.value},
    )
