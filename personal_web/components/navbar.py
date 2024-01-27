import reflex as rx

from personal_web.styles.colors import Color
from personal_web.styles.styles import NAVBAR_TITLE_STYLE, Size


def navbar() -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.span(
                "juanda",
                color=Color.PRIMARY.value,
                _hover={"text_shadow": f"0 0 8px {Color.PRIMARY.value}"},
            ),
            rx.span(
                "herrera",
                color=Color.SECONDARY.value,
                _hover={"text_shadow": f"0 0 8px {Color.SECONDARY.value}"},
            ),
            style=NAVBAR_TITLE_STYLE,
        ),
        position="sticky",
        bg=Color.CONTENT.value,
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index="999",
        top="0",
        width="100%",
        box_shadow="0 6px 55px 0 rgba(255, 107, 107, 0.2)",
    )
