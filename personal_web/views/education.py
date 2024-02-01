import reflex as rx

import personal_web.styles.styles as styles
from personal_web.components.education import college_degree
from personal_web.components.texts import title
from personal_web.data.education import education_list
from personal_web.styles.styles import Size


def education() -> rx.Component:
    return rx.vstack(
        title("Educación 📖"),
        rx.flex(
            *[college_degree(degree) for degree in education_list],
            flex_wrap="wrap",
        ),
        align_items="start",
        spacing=Size.DEFAULT_BIG.value,
        style=styles.INDEX_SECTION_STYLE,
    )
