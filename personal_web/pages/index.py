import reflex as rx

import personal_web.constants as const
import personal_web.utils as utils
from personal_web.components.footer import footer
from personal_web.components.navbar import navbar
from personal_web.styles.colors import Color
from personal_web.styles.styles import Size
from personal_web.views.about_me import about_me
from personal_web.views.courses import courses
from personal_web.views.education import education
from personal_web.views.experience import experience
from personal_web.views.presentation import presentation
from personal_web.views.projects import projects
from personal_web.views.technologies import technologies


@rx.page(
    title=const.INDEX_TILE,
    description=const.INDEX_DESCRIPTION,
    image=const.INDEX_PREVIEW,
    meta=const.INDEX_META,
)
def index() -> rx.Component:
    return rx.vstack(
        utils.lang(),
        navbar(),
        presentation(),
        about_me(),
        technologies(),
        experience(),
        rx.vstack(
            projects(),
            education(),
            courses(),
            footer(),
            width="100%",
            background=Color.BACKGROUND_ALT.value,
            box_shadow=f"0 0 {Size.DEFAULT_BIG.value} {Color.CONTENT.value}",
        ),
        width="100%",
    )
