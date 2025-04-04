import reflex as rx
import reflex_chakra as rxc

from personal_web.components.buttons import rounded_button
from personal_web.components.texts import title
from personal_web.components.work_experience import tech_badge
from personal_web.data.courses import Course, School
from personal_web.state import MainState
from personal_web.styles import styles
from personal_web.styles.colors import Color, TextColor
from personal_web.styles.fonts import FontSize
from personal_web.styles.styles import Size


def school(school: School) -> rx.Component:
    return rxc.accordion(
        rxc.accordion_item(
            rxc.accordion_button(
                _school_header(school.name, school.logo, school.courses_qty),
                _hover={},
            ),
            rxc.accordion_panel(
                rx.grid(
                    *[course(item) for item in school.courses],
                    columns=rx.breakpoints(
                        initial="1",
                        sm="2",
                        md="3",
                    ),
                    width="100%",
                    spacing="5",
                    padding_top=Size.DEFAULT_BIG.value,
                )
            ),
            border_width=Size.ZERO.value,
        ),
        allow_toggle=True,
        style=styles.SCHOOL_ACCORDION_STYLE,
    )


def course(course: Course) -> rx.Component:
    return rxc.card(
        rx.flex(
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
    return rx.vstack(
        title(
            name,
            size="5",
        ),
        rx.text(
            issue_date,
            font_size=FontSize.SMALL_TEXT.value,
            color=Color.SECONDARY.value,
        ),
        align_items="start",
        spacing="0",
    )


def _school_header(name: str, logo: str, courses_qty: int) -> rx.Component:
    return rx.hstack(
        rx.image(
            src=logo,
            height=Size.VERY_BIG.value,
            width="auto",
            min_width=Size.VERY_BIG.value,
            loading="lazy",
        ),
        rxc.divider(
            orientation="vertical",
            border_color=TextColor.PRIMARY.value,
            height=Size.VERY_BIG.value,
        ),
        rx.vstack(
            title(
                name,
                size="6",
            ),
            rx.text(
                rx.text.span(courses_qty, color=Color.SECONDARY.value),
                rx.cond(
                    MainState.is_language_en,
                    " Completed Courses",
                    " Cursos Finalizados",
                ),
                font_size=FontSize.BODY.value,
                text_align="left",
            ),
            align_items="start",
            spacing="0",
        ),
        rx.spacer(),
        rxc.accordion_icon(font_size=Size.BIG.value, style=styles.ACCORDION_ICON_STYLE),
        align_items="center",
        width="100%",
        spacing="5",
    )
