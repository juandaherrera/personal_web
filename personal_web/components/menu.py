import reflex as rx

from personal_web.state import MainState
from personal_web.styles.colors import Color, TextColor
from personal_web.styles.styles import Size

from .language_switch import language_switch


def menu() -> rx.Component:
    return rx.menu.root(
        rx.menu.trigger(
            rx.icon_button(
                "menu",
                color_scheme="gray",
                variant="soft",
                size="3",
                bg=Color.BACKGROUND_ALT.value,
                _hover={"cursor": "pointer"},
            ),
        ),
        rx.menu.content(
            rx.menu.item(
                language_switch(),
                padding_y=Size.SMALL.value,
                display=["block", "block", "block", "none"],
            ),
            rx.menu.separator(display=["block", "block", "block", "none"]),
            _menu_item(
                rx.cond(MainState.is_language_en, "About me", "Acerca de mí"),
                "👨🏻‍💻",
                "#about_me",
            ),
            _menu_item(
                rx.cond(MainState.is_language_en, "Work Experience", "Experiencia"),
                "💼",
                "#experience",
            ),
            _menu_item(
                rx.cond(MainState.is_language_en, "Projects", "Proyectos"), "💻", "#projects"
            ),
            rx.menu.separator(),
            _menu_item(
                rx.cond(MainState.is_language_en, "Education", "Educación"), "📖", "#education"
            ),
            _menu_item(
                rx.cond(MainState.is_language_en, "Certifications", "Certificaciones"),
                "📃",
                "#certifications",
            ),
            _menu_item(rx.cond(MainState.is_language_en, "Courses", "Cursos"), "📝", "#courses"),
            side="bottom",
            side_offset=10,
            align="end",
        ),
    )


def _menu_item(text: str, emoji: str, url: str, is_external: bool = False) -> rx.Component:
    return rx.menu.item(
        rx.link(
            rx.text(
                text,
                color=TextColor.PRIMARY.value,
            ),
            href=url,
            is_external=is_external,
        ),
        shortcut=emoji,
    )
