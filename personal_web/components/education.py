import reflex as rx

from personal_web.components.texts import title
from personal_web.data.education import Degree
from personal_web.styles.colors import Color
from personal_web.styles.fonts import FontSize
from personal_web.styles.styles import Size


def college_degree(degree: Degree) -> rx.Component:
    return rx.hstack(
        rx.center(
            rx.image(
                src=degree.college_logo,
                alt=f"Logo de {degree.college}",
                height="5em",
            ),
        ),
        rx.vstack(
            title(
                degree.title,
                font_size=FontSize.SUBTITLES.value,
            ),
            rx.text(
                degree.college,
                font_size=FontSize.BODY.value,
                color=Color.SECONDARY.value,
            ),
            rx.text(
                degree.period,
                font_size=FontSize.SMALL_TEXT.value,
            ),
            align_items="start",
            spacing=Size.ZERO.value,
        ),
        spacing=Size.DEFAULT.value,
        margin_right=[Size.DEFAULT_BIG.value, Size.VERY_BIG.value],
        margin_bottom=[Size.DEFAULT_BIG.value, Size.VERY_BIG.value],
    )
