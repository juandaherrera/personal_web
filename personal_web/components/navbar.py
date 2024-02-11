import reflex as rx

import personal_web.styles.styles as styles
from personal_web.styles.colors import Color
from personal_web.styles.styles import Size
from personal_web.utils import hex_to_rgb


def navbar() -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.span(
                "juanda",
                color=Color.PRIMARY.value,
                transition="text-shadow 0.5s ease",
                _hover={
                    "text_shadow": f"0 0 8px {Color.SECONDARY.value}",
                },
            ),
            rx.span(
                "herrera",
                color=Color.SECONDARY.value,
                transition="text-shadow 0.5s ease",
                _hover={
                    "text_shadow": f"0 0 8px {Color.PRIMARY.value}",
                },
            ),
            style=styles.NAVBAR_TITLE_STYLE,
        ),
        rx.spacer(),
        rx.menu(
            rx.menu_button(
                rx.icon(tag="hamburger", font_size=Size.DEFAULT_BIG.value)
            ),
            rx.menu_list(
                _menu_item("Acerca de mí 👨🏻‍💻", "#about_me"),
                _menu_item("Experiencia 💼", "#experience"),
                _menu_item("Proyectos 💻", "#projects"),
                rx.menu_divider(),
                _menu_item("Educación 📖", "#education"),
                _menu_item("Cursos 📝", "#courses"),
                background=Color.CONTENT.value,
                border_color=Color.BACKGROUND.value,
            ),
        ),
        style=styles.NAVBAR_STYLE,
        box_shadow=f"0 {Size.VERY_SMALL.value} {Size.BIG.value} 0 {hex_to_rgb(Color.PRIMARY.value, 0.2)}",
    )


def _menu_item(text: str, url: str, is_external: bool = False) -> rx.Component:
    return rx.menu_item(
        rx.link(rx.text(text), href=url, is_external=is_external),
        background="transparent",
        transition="color 0.2s ease",
        _hover={"color": Color.SECONDARY.value},
    )
