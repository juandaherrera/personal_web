import reflex as rx

from personal_web.components.footer import footer
from personal_web.components.navbar import navbar
from personal_web.views.about_me import about_me
from personal_web.views.presentation import presentation


@rx.page()
def index() -> rx.Component:
    return rx.vstack(
        navbar(),
        presentation(),
        about_me(),
        footer(),
        width="100%",
    )
