import reflex as rx

import personal_web.styles.styles as styles
from personal_web.components.texts import title
from personal_web.components.work_experience import work_experience
from personal_web.data.job import work_experience_en_list, work_experience_list
from personal_web.state import MainState
from personal_web.styles.styles import Size


def experience(en: bool = False) -> rx.Component:
    selected_list = work_experience_list if not en else work_experience_en_list
    return rx.vstack(
        title("Work Experience 💼" if en else "Experiencia 💼"),
        *[work_experience(item) for item in selected_list],
        align_items="start",
        spacing="5",
        style=styles.INDEX_SECTION_STYLE,
        padding_bottom=Size.LARGE.value,
        id="experience",
    )
