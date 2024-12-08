import reflex as rx


class MainState(rx.State):
    is_language_en: bool = False

    @rx.event
    def toggle_language(self):
        self.is_language_en = not self.is_language_en
