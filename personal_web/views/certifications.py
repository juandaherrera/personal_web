import reflex as rx

import personal_web.styles.styles as styles
from personal_web.components.certification import certification
from personal_web.components.texts import title
from personal_web.data.certification import certifications_en_list, certifications_list
from personal_web.styles.styles import Size


def certifications(en: bool = False) -> rx.Component:
    selected_list = certifications_en_list if en else certifications_list
    return rx.vstack(
        title("Certifications 📃" if en else "Certificaciones 📃"),
        rx.grid(
            *[certification(item) for item in selected_list],
            width="100%",
            spacing_x="5",
            spacing_y="8",
            columns=rx.breakpoints(
                initial="1",
                sm="2",
                md="3",
            ),
        ),
        align_items="start",
        spacing="4",
        style=styles.INDEX_SECTION_STYLE,
        padding_top=Size.LARGE.value,
        id="certifications",
    )
