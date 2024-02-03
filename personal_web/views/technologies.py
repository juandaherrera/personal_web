import reflex as rx

from personal_web.components.techstack import techstack
from personal_web.data.personal_info import TECHSTACK
from personal_web.styles.styles import Size


def technologies() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.hstack(
                *[
                    techstack(src=name, url=url, is_class=is_class)
                    for name, is_class, url in TECHSTACK
                ],
                class_name="logos-slide"
            ),
            rx.hstack(
                *[
                    techstack(src=name, url=url, is_class=is_class)
                    for name, is_class, url in TECHSTACK
                ],
                class_name="logos-slide"
            ),
            class_name="logos",
            width="100%",
            padding_y=Size.DEFAULT_MEDIUM.value,
        ),
        width="100%",
    )
