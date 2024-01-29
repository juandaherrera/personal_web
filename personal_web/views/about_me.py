import reflex as rx

from personal_web.components.texts import title
from personal_web.data.personal_info import ABOUT_ME
from personal_web.styles.styles import Size


def about_me() -> rx.Component:
    return rx.vstack(
        # TO_DO lógica para scrollear hasta aquí
        title("Acerca de mi 👨🏻‍💻", id="about_me"),
        rx.text(
            ABOUT_ME, text_align="justify", font_size=Size.DEFAULT_MEDIUM.value
        ),
        align_items="start",
        max_width="85em",
        padding_x=Size.VERY_BIG.value,
        padding_y=Size.VERY_BIG.value,
    )
