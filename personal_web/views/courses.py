import reflex as rx

import personal_web.styles.styles as styles
from personal_web.components.course import school
from personal_web.components.texts import title
from personal_web.data.courses import schools_list
from personal_web.styles.colors import Color
from personal_web.styles.styles import FontSize, Size

total_courses = sum([item.courses_qty for item in schools_list])


def courses() -> rx.Component:
    return rx.chakra.vstack(
        title("Cursos 📝", margin_bottom=Size.ZERO.value),
        rx.chakra.text(
            "Total cursos finalizados: ",
            rx.chakra.span(total_courses, color=Color.SECONDARY.value),
            font_size=FontSize.SECOND_SUBTITLE.value,
        ),
        *[school(item) for item in schools_list],
        align_items="start",
        spacing=Size.DEFAULT_BIG.value,
        style=styles.INDEX_SECTION_STYLE,
        padding_top=Size.LARGE.value,
        id="courses",
    )
