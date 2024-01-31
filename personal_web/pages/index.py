import reflex as rx

import personal_web.constants as const
from personal_web.components.footer import footer
from personal_web.components.navbar import navbar
from personal_web.views.about_me import about_me
from personal_web.views.experience import experience
from personal_web.views.presentation import presentation
from personal_web.views.technologies import technologies


@rx.page(
    title=const.INDEX_TILE,
    description=const.INDEX_DESCRIPTION,
    image=const.INDEX_PREVIEW,
    meta=const.INDEX_META,
)
def index() -> rx.Component:
    return rx.vstack(
        navbar(),
        presentation(),
        about_me(),
        technologies(),
        experience(),
        footer(),
        width="100%",
    )
