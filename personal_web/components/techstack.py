import reflex as rx

from personal_web.styles.colors import Color
from personal_web.styles.styles import Size


# TO_DO fix para que las imagenes y los iconos tengan el mismo padding/espaciado
def techstack(src: str, url: str = "/", is_class: bool = True) -> rx.Component:
    return rx.cond(
        is_class,
        rx.link(
            rx.box(
                class_name=f"devicon-{src}-plain",
                font_size=Size.LARGE.value,
                padding_x=Size.MEDIUM.value,
                _hover={
                    "color": Color.SECONDARY.value,
                    "text_shadow": f"0 0 6px {Color.PRIMARY.value}",
                },
            ),
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
