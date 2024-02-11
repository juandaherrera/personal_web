import reflex as rx

import personal_web.styles.styles as styles
from personal_web.components.course import school
from personal_web.components.texts import title
from personal_web.data.courses import schools_list
from personal_web.styles.styles import Size


def courses() -> rx.Component:
    return rx.vstack(
        title("Cursos 📝"),
        *[school(item) for item in schools_list],
        align_items="start",
        spacing=Size.DEFAULT_BIG.value,
        style=styles.INDEX_SECTION_STYLE,
        padding_top=Size.BIG.value,
    )
