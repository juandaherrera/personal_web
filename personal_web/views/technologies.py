import reflex as rx

from personal_web.components.techstack import techstack
from personal_web.data.personal_info import TECHSTACK
from personal_web.styles.styles import Size


def technologies() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.center(
                *[
                    techstack(src=name, url=url, is_class=is_class)
                    for name, is_class, url in TECHSTACK
                ],
                width="100%",
            ),
        ),
        width="100%",
        padding_bottom=Size.VERY_BIG.value,
    )
