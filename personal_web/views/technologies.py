import reflex as rx

from personal_web.components.techstack import techstack
from personal_web.data.technologies import tech_list
from personal_web.styles.styles import Size


def technologies() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.hstack(*[techstack(tech) for tech in tech_list], class_name="logos-slide"),
            rx.hstack(*[techstack(tech) for tech in tech_list], class_name="logos-slide"),
            class_name="logos",
            width="100%",
            padding_y=Size.DEFAULT_MEDIUM.value,
        ),
        width="100%",
    )
