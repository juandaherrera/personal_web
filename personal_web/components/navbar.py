import reflex as rx

from personal_web.components.language_switch import language_switch
from personal_web.components.menu import menu
from personal_web.styles import styles
from personal_web.styles.colors import Color
from personal_web.styles.styles import Size
from personal_web.utils import hex_to_rgb


def navbar() -> rx.Component:
    return rx.hstack(
        rx.flex(
            rx.text(
                "juanda",
                color=Color.PRIMARY.value,
                transition="text-shadow 0.5s ease",
                _hover={
                    "text_shadow": f"0 0 8px {Color.SECONDARY.value}",
                    "cursor": "default",
                },
            ),
            rx.text(
                "herrera",
                color=Color.SECONDARY.value,
                transition="text-shadow 0.5s ease",
                _hover={
                    "text_shadow": f"0 0 8px {Color.PRIMARY.value}",
                    "cursor": "default",
                },
            ),
            style=styles.NAVBAR_TITLE_STYLE,
        ),
        rx.spacer(),
        rx.hstack(
            rx.desktop_only(language_switch()),
            menu(),
            spacing="6",
            align="center",
        ),
        style=styles.NAVBAR_STYLE,
        box_shadow=f"0 {Size.VERY_SMALL.value} {Size.BIG.value} 0 {hex_to_rgb('#FF6B6B', 0.2)}",
    )
