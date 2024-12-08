import reflex as rx

from personal_web.state import MainState


def language_switch() -> rx.Component:
    return rx.tooltip(
        rx.hstack(
            rx.text("ES", size="2"),
            rx.switch(
                checked=MainState.is_language_en,
                on_change=MainState.toggle_language,
                color_scheme="red",
                _hover={
                    "cursor": "pointer",
                },
            ),
            rx.text("EN", size="2"),
            spacing="2",
            align="center",
        ),
        content=rx.cond(MainState.is_language_en, "Cambiar a Español", "Change to English"),
        side_offset=10,
    )
