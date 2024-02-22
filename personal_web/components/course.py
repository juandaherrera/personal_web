import reflex as rx

import personal_web.styles.styles as styles
from personal_web.components.texts import title
from personal_web.components.work_experience import tech_badge
from personal_web.data.courses import Course, School
from personal_web.styles.colors import Color, TextColor
from personal_web.styles.fonts import FontSize
from personal_web.styles.styles import Size
from personal_web.utils import hex_to_rgb

from .buttons import rounded_button


def school(school: School) -> rx.Component:
    return rx.chakra.accordion(
        rx.chakra.accordion_item(
            rx.chakra.accordion_button(
                _school_header(school.name, school.logo, school.courses_qty),
                _hover={},
            ),
            rx.chakra.accordion_panel(
                rx.chakra.responsive_grid(
                    *[course(item) for item in school.courses],
                    columns=[1, 1, 2, 3, 3],
                    width="100%",
                    spacing=Size.DEFAULT_BIG.value,
                    padding_top=Size.DEFAULT_BIG.value,
                )
            ),
            border_width=Size.ZERO.value,
        ),
        allow_toggle=True,
        style=styles.SCHOOL_ACCORDION_STYLE,
    )


def course(course: Course) -> rx.Component:
    return rx.chakra.card(
        rx.chakra.flex(
            *[tech_badge(item) for item in course.technologies],
            padding_y=Size.ZERO.value,
            flex_wrap="wrap",
        ),
        header=_course_header(course.name, course.issue_date_format),
        footer=rounded_button(
            "Credencial",
            url=course.credential_url,
            margin_top=Size.ZERO.value,
        ),
        style=styles.COURSE_CARD_STYLE,
    )


def _course_header(name: str, issue_date: str):
    return rx.chakra.vstack(
        title(
            name,
            margin_bottom=Size.ZERO.value,
            font_size=FontSize.SECOND_SUBTITLE.value,
        ),
        rx.chakra.text(
            issue_date,
            font_size=FontSize.SMALL_TEXT.value,
            color=Color.SECONDARY.value,
        ),
        align_items="start",
        spacing=Size.SMALL.value,
    )


def _school_header(name: str, logo: str, courses_qty: int) -> rx.Component:
    return rx.chakra.hstack(
        rx.chakra.image(
            src=logo, height=Size.VERY_BIG.value, min_width=Size.VERY_BIG.value
        ),
        rx.chakra.divider(
            orientation="vertical",
            border_color=TextColor.PRIMARY.value,
            height=Size.VERY_BIG.value,
        ),
        rx.chakra.vstack(
            title(
                name,
                font_size=FontSize.SUBTITLES.value,
                margin_bottom=Size.ZERO.value,
            ),
            rx.chakra.text(
                rx.chakra.span(courses_qty, color=Color.SECONDARY.value),
                " Cursos Finalizados",
                font_size=FontSize.BODY.value,
                text_align="left",
            ),
            align_items="start",
            spacing=Size.VERY_SMALL.value,
        ),
        rx.chakra.spacer(),
        rx.chakra.accordion_icon(
            font_size=Size.BIG.value, style=styles.ACCORDION_ICON_STYLE
        ),
        align_items="center",
        width="100%",
        spacing=Size.DEFAULT.value,
    )
