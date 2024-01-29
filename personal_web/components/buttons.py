import reflex as rx

import personal_web.styles.styles as styles
from personal_web.styles.colors import Color, TextColor
from personal_web.styles.styles import Size


# TO_DO Arreglar este botón para que solo sea com bordes y sin fondo
def default_button(
    text: str, icon: str, button_color: str, text_color: str
) -> rx.Component:
    return rx.button(
        rx.hstack(
            rx.text(text),
            rx.icon(tag=icon),
            font_size=Size.DEFAULT_BIG.value,
            color=text_color,
            padding_x=Size.MEDIUM.value,
        ),
        style=styles.DEFAULT_BUTTON_STYLE,
        border_color=button_color,
        _hover={
            "background_color": "transparent",
            "box_shadow": f"0 0 8px {button_color}, 0 0 12px {button_color}",
        },
    )
