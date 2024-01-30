import reflex as rx

from personal_web.styles.styles import Size


# TO_DO fix para que las imagenes y los iconos tengan el mismo padding/espaciado
def techstack(src: str, url: str = "/", is_class: bool = True) -> rx.Component:
    return rx.cond(
        is_class,
        rx.box(
            class_name=f"devicon-{src}-plain",
            font_size=Size.VERY_BIG.value,
            padding_x="0.12em",
        ),
        rx.box(
            rx.image(
                src=src, height=Size.VERY_BIG.value, width=Size.VERY_BIG.value
            ),
            padding_x="0.48em",
        ),
    )
