import reflex as rx

import personal_web.styles.styles as styles
from personal_web.components.texts import title
from personal_web.data.personal_info import ABOUT_ME
from personal_web.styles.fonts import FontSize
from personal_web.styles.styles import Size


def about_me() -> rx.Component:
    return rx.vstack(
        title("Acerca de mí 👨🏻‍💻"),
        rx.text(
            ABOUT_ME,
            text_align="justify",
            font_size=FontSize.BODY.value,
        ),
        align_items="start",
        style=styles.INDEX_SECTION_STYLE,
        padding_bottom=Size.VERY_BIG.value,
        id="about_me",
    )
