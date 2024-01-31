import reflex as rx

import personal_web.styles.styles as styles
from personal_web.components.texts import title
from personal_web.components.work_experience import work_experience
from personal_web.data.job import work_experience_list
from personal_web.styles.colors import Color
from personal_web.styles.styles import Size


def experience() -> rx.Component:
    return rx.vstack(
        title("Experiencia 💻"),
        *[work_experience(item) for item in work_experience_list],
        align_items="start",
        spacing=Size.DEFAULT_BIG.value,
        style=styles.INDEX_SECTION_STYLE,
    )
