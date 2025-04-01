import reflex as rx

from personal_web.components.education import college_degree
from personal_web.components.texts import title
from personal_web.data.education import education_en_list, education_list
from personal_web.styles import styles


def education(en: bool = False) -> rx.Component:
    selected_list = education_list if not en else education_en_list
    return rx.vstack(
        title("Education 📖" if en else "Educación 📖"),
        rx.grid(
            *[college_degree(degree) for degree in selected_list],
            columns=rx.breakpoints(
                initial="1",
                sm="2",
                lg="3",
            ),
            spacing_x="5",
            spacing_y="2",
        ),
        align_items="start",
        spacing="5",
        style=styles.INDEX_SECTION_STYLE,
        id="education",
    )
