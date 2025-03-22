import reflex as rx

from personal_web.components.course import school
from personal_web.components.texts import title
from personal_web.data.courses import schools_en_list, schools_list
from personal_web.styles import styles
from personal_web.styles.colors import Color
from personal_web.styles.styles import FontSize, Size

total_courses = sum([item.courses_qty for item in schools_list])


def courses(en: bool = False) -> rx.Component:
    selected_list = schools_list if not en else schools_en_list
    return rx.vstack(
        title(
            "Courses 📝" if en else "Cursos 📝",
            margin_bottom=Size.ZERO.value,
        ),
        rx.text(
            "Total completed courses: " if en else "Total cursos finalizados: ",
            rx.text.span(
                total_courses,
                color=Color.SECONDARY.value,
            ),
            font_size=FontSize.SECOND_SUBTITLE.value,
        ),
        *[school(item) for item in selected_list],
        align_items="start",
        spacing="5",
        style=styles.INDEX_SECTION_STYLE,
        padding_top=Size.LARGE.value,
        id="courses",
    )
