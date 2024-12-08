import reflex as rx

from personal_web.components.texts import title
from personal_web.data.education import Degree
from personal_web.styles.colors import Color
from personal_web.styles.fonts import FontSize
from personal_web.styles.styles import EDUCATION_COLLEGE_LOGO_STYLE, Size


def college_degree(degree: Degree) -> rx.Component:
    return rx.hstack(
        rx.center(
            rx.image(
                src=degree.college_logo,
                alt=f"Logo de {degree.college}",
                style=EDUCATION_COLLEGE_LOGO_STYLE,
            ),
        ),
        rx.vstack(
            title(
                degree.title,
                font_size=FontSize.SUBTITLES.value,
                margin_bottom=Size.ZERO.value,
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
            spacing="0",
            max_width=["90%", "85%", "80%", "80%", "75%"],
        ),
        align="center",
        spacing="3",
    )
