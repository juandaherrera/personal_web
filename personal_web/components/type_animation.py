from typing import Union

import reflex as rx
from reflex.vars import Var

from personal_web.styles.colors import TextColor
from personal_web.styles.styles import Size


class TypeAnimation(rx.Component):
    """Texts that are written and erased dynamically."""

    library = "react-type-animation"
    tag = "TypeAnimation"
    sequence: Var[list]
    speed: Var[int] = 40
    repeat: Var[Union[int, float]] = 0
    cursor: Var[bool] = True


type_animation = TypeAnimation.create
