import reflex as rx

from personal_web.styles.colors import Color
from personal_web.styles.styles import TECH_STACK_STYLE, Size


# TO_DO fix para que las imagenes y los iconos tengan el mismo padding/espaciado
def techstack(src: str, url: str = "/", is_class: bool = True) -> rx.Component:
    return rx.cond(
        is_class,
        rx.link(
            rx.box(class_name=f"devicon-{src}-plain", style=TECH_STACK_STYLE),
            href=url,
            is_external=True,
        ),
        rx.box(
            rx.image(
                src=src, height=Size.VERY_BIG.value, width=Size.VERY_BIG.value
            ),
            padding_x=Size.VERY_BIG.value,
        ),
    )
