import reflex as rx

from personal_web.components.texts import title
from personal_web.data.personal_info import ABOUT_ME
from personal_web.state import MainState
from personal_web.styles import styles
from personal_web.styles.fonts import FontSize
from personal_web.styles.styles import Size


def about_me() -> rx.Component:
    return rx.vstack(
        title(rx.cond(MainState.is_language_en, "About me 👨🏻‍💻", "Acerca de mí 👨🏻‍💻")),
        rx.text(
            ABOUT_ME,
            text_align="justify",
            font_size=FontSize.BODY.value,
        ),
        spacing="2",
        align_items="start",
        style=styles.INDEX_SECTION_STYLE,
        padding_bottom=Size.VERY_BIG.value,
        id="about_me",
    )
