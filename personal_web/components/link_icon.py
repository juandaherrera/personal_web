import reflex as rx

from personal_web.styles.styles import Size


def link_icon(image: str, url: str, alt: str) -> rx.Component:
    return rx.link(
        rx.image(
            src=image,
            width=Size.BIG.value,
            height=Size.BIG.value,
            alt=alt,
        ),
        href=url,
        is_external=True,
    )
