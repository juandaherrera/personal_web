import reflex as rx

from personal_web.components.texts import title
from personal_web.data.education import Degree
from personal_web.styles.colors import Color
from personal_web.styles.fonts import FontSize
from personal_web.styles.styles import EDUCATION_COLLEGE_LOGO_STYLE, Size


def college_degree(degree: Degree) -> rx.Component:
    return rx.chakra.hstack(
        rx.chakra.center(
            rx.chakra.image(
                src=degree.college_logo,
                alt=f"Logo de {degree.college}",
                style=EDUCATION_COLLEGE_LOGO_STYLE,
            ),
        ),
        rx.chakra.vstack(
            title(
                degree.title,
                font_size=FontSize.SUBTITLES.value,
            ),
            rx.chakra.text(
                degree.college,
                font_size=FontSize.BODY.value,
                color=Color.SECONDARY.value,
            ),
            rx.chakra.text(
                degree.period,
                font_size=FontSize.SMALL_TEXT.value,
            ),
            align_items="start",
            spacing=Size.ZERO.value,
            max_width=["90%", "85%", "80%", "80%", "75%"],
        ),
        spacing=Size.DEFAULT.value,
    )
