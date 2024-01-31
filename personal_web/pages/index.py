import reflex as rx

from personal_web.components.footer import footer
from personal_web.components.navbar import navbar
from personal_web.views.about_me import about_me
from personal_web.views.experience import experience
from personal_web.views.presentation import presentation
from personal_web.views.technologies import technologies


@rx.page()
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
