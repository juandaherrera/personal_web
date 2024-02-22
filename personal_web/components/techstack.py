import reflex as rx

from personal_web.data.technologies import Technology
from personal_web.styles.styles import (
    TECH_STACK_ICON_STYLE,
    TECH_STACK_STYLE,
    Size,
)


def techstack(technology: Technology) -> rx.Component:
    return rx.chakra.link(
        rx.chakra.vstack(
            rx.chakra.box(
                class_name=f"devicon-{technology.icon}-plain",
                style=TECH_STACK_ICON_STYLE,
            ),
            rx.chakra.text(technology.name, padding_top=Size.SMALL.value),
            align_items="center",
            style=TECH_STACK_STYLE,
        ),
        href=technology.url,
        is_external=True,
    )
