import reflex as rx

import personal_web.constants as const
from personal_web import utils
from personal_web.components.footer import footer
from personal_web.components.navbar import navbar
from personal_web.state import MainState
from personal_web.styles.colors import Color
from personal_web.styles.styles import Size
from personal_web.views import (
    about_me,
    certifications,
    courses,
    education,
    experience,
    presentation,
    projects,
    recommendations,
    technologies,
)


@rx.page(
    title=const.INDEX_TILE,
    description=const.INDEX_DESCRIPTION,
    image=const.INDEX_PREVIEW,
    meta=const.INDEX_META,
    on_load=MainState.calculate_durations,
)
def index() -> rx.Component:
    return rx.vstack(
        utils.lang(),
        navbar(),
        presentation(),
        about_me(),
        technologies(),
        rx.cond(MainState.is_language_en, experience(en=True), experience()),
        rx.vstack(
            rx.cond(MainState.is_language_en, projects(en=True), projects()),
            rx.cond(MainState.is_language_en, education(en=True), education()),
            rx.cond(MainState.is_language_en, certifications(en=True), certifications()),
            rx.cond(MainState.is_language_en, courses(en=True), courses()),
            align="center",
            width="100%",
            padding_bottom=Size.LARGE.value,
            background=Color.BACKGROUND_ALT.value,
            box_shadow=f"0 0 {Size.DEFAULT_BIG.value} {Color.CONTENT.value}",
        ),
        recommendations(),
        # rx.cond(MainState.is_language_en, contact(en=True), contact()),
        footer(),
        spacing="0",
        align="center",
        width="100%",
    )
