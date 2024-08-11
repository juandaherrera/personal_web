import reflex as rx

from personal_web.pages import index
from personal_web.styles.styles import BASE_STYLE, STYLESHEETS

app = rx.App(theme=rx.theme(appearance="dark"), style=BASE_STYLE, stylesheets=STYLESHEETS)
