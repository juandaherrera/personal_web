import reflex as rx

import personal_web.styles.styles as styles
from personal_web.styles.colors import Color
from personal_web.styles.styles import Size
from personal_web.utils import hex_to_rgb

from .menu import menu


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
        menu(),
        style=styles.NAVBAR_STYLE,
        box_shadow=f"0 {Size.VERY_SMALL.value} {Size.BIG.value} 0 {hex_to_rgb(Color.PRIMARY.value, 0.2)}",
    )
