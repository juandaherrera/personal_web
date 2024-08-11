import reflex as rx

from personal_web.styles.colors import Color, TextColor
from personal_web.styles.styles import Size


def menu() -> rx.Component:
    return rx.chakra.menu(
        rx.chakra.menu_button(
            rx.chakra.icon(
                tag="hamburger",
                font_size=Size.DEFAULT_BIG.value,
            ),
            style=dict(
                border_radius="50px",
                border=f"1px solid {rx.color('mauve', 4)}",
                background=Color.BACKGROUND_ALT.value,
                box_shadow="0px 3px 7px -4px rgba(21, 18, 44, 0.15)",
                padding="7px 12px 7px 12px",
                align_items="center",
            ),
            border_radius="8px",
            color=rx.color("mauve", 9),
            transition="color 0.2s ease",
            _hover={
                "color": Color.SECONDARY.value,
            },
        ),
        rx.chakra.menu_list(
            _menu_item("Acerca de mí", "👨🏻‍💻", "#about_me"),
            _menu_item("Experiencia", "💼", "#experience"),
            _menu_item("Proyectos", "💻", "#projects"),
            rx.chakra.menu_divider(),
            _menu_item("Educación", "📖", "#education"),
            _menu_item("Certificaciones", "📃", "#certifications"),
            _menu_item("Cursos", "📝", "#courses"),
            background=Color.BACKGROUND_ALT.value,
            border_color=rx.color('mauve', 1),
        ),
    )


# TO_DO revisar emojis a la derecha del todo
def _menu_item(text: str, emoji: str, url: str, is_external: bool = False) -> rx.Component:
    return rx.chakra.menu_item(
        rx.link(
            rx.text(
                f"{text} ",
                rx.text.span(f"{emoji}"),
                _hover={"color": Color.SECONDARY.value},
            ),
            href=url,
            is_external=is_external,
            color=TextColor.PRIMARY.value,
        ),
        background="transparent",
        transition="color 0.2s ease",
    )
