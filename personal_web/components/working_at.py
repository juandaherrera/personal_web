import reflex as rx

from personal_web.state import MainState
from personal_web.styles.styles import Size


def working_at(image: str, url: str, alt: str) -> rx.Component:
    return rx.hstack(
        rx.text(
            rx.cond(MainState.is_language_en, "At", "En"),
            font_size=[Size.DEFAULT_BIG.value, Size.BIG.value],
        ),
        rx.link(
            rx.image(
                src=image,
                alt=alt,
                height=["2em", "2.5em"],
                width="auto",
                transition="transform 0.2s ease",
                _hover={
                    "transform": "scale(1.1)",
                },
            ),
            href=url,
            is_external=True,
        ),
        align="center",
        spacing="2",
        padding_bottom=Size.DEFAULT_MEDIUM.value,
    )
