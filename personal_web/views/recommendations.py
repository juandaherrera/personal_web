import reflex as rx

from personal_web.components.bento_card import bento_card
from personal_web.components.texts import title
from personal_web.styles import styles


def recommendations() -> rx.Component:
    return rx.vstack(
        title("Recommendations"),
        rx.text("This is the recommendations section."),
        rx.grid(
            rx.vstack(
                bento_card(),
                bento_card(),
                spacing="5",
            ),
            bento_card(),
            columns="2",
            spacing="5",
            width="100%",
        ),
        style=styles.INDEX_SECTION_STYLE,
        spacing="6",
        align_items="start",
        id="recommendations",
    )
