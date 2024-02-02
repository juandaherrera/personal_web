import reflex as rx

from personal_web.styles.styles import Size


def working_at(image: str, url: str, alt: str) -> rx.Component:
    return rx.hstack(
        rx.text("En", font_size=[Size.DEFAULT_BIG.value, Size.BIG.value]),
        rx.link(
            rx.image(src=image, alt=alt, height=["2em", "2.5em"]),
            href=url,
            is_external=True,
        ),
        padding_bottom=Size.DEFAULT_MEDIUM.value,
    )
