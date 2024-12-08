import reflex as rx

import personal_web.styles.styles as styles
from personal_web.components.texts import title
from personal_web.components.work_experience import company_experience
from personal_web.data.job import resume, resume_en
from personal_web.state import MainState
from personal_web.styles.styles import Size


def experience(en: bool = False) -> rx.Component:
    selected_obj = resume if not en else resume_en
    return rx.vstack(
        title("Work Experience 💼" if en else "Experiencia 💼"),
        rx.vstack(
            *[company_experience(company, en) for company in selected_obj.companies],
            spacing="5",
            width="100%",
        ),
        align_items="start",
        spacing="5",
        style=styles.INDEX_SECTION_STYLE,
        padding_bottom=Size.LARGE.value,
        id="experience",
    )
