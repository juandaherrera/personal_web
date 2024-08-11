import reflex as rx

import personal_web.styles.styles as styles
from personal_web.components.education import college_degree
from personal_web.components.texts import title
from personal_web.data.education import education_list
from personal_web.styles.styles import Size


def education() -> rx.Component:
    return rx.vstack(
        title("Educación 📖"),
        rx.grid(
            *[college_degree(degree) for degree in education_list],
            columns=rx.breakpoints(
                initial="1",
                sm="2",
                lg="3",
            ),
            spacing_x=Size.DEFAULT_BIG.value,
            spacing_y=Size.MEDIUM_BIG.value
        ),
        align_items="start",
        spacing=Size.DEFAULT_BIG.value,
        style=styles.INDEX_SECTION_STYLE,
        id="education",
    )
