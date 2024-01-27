import reflex as rx

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
            padding_y=Size.DEFAULT_BIG.value,
        ),
        variant="ghost",
        background_color=button_color,
        border=Size.BIG.value,
        border_color=button_color,
    )
