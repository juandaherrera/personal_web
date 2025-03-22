from reflex import cond

from personal_web.state import MainState
from personal_web.utils import get_experience

SPANISH_ABOUT_ME = f"""
Soy Ingeniero Industrial y Python Developer con más de {get_experience()} años de experiencia en
 ingeniería de datos y desarrollo de microservicios para áreas de Producción/Operaciones.
 Mi enfoque principal está en el diseño y desarrollo de soluciones innovadoras utilizando Python,
 con un interés especial en construir aplicaciones robustas y eficientes que optimicen procesos y
 resuelvan problemas complejos. Actualmente en Rappi, me involucro activamente en proyectos de
 Data Engineering y Python Development, aplicando mis conocimientos avanzados en SQL, Python,
 FastAPI, Apache Airflow y Snowflake.
"""

ENGLISH_ABOUT_ME = f"""
I am an Industrial Engineer and Python Developer with over {get_experience()} years of experience
 in data engineering and microservices development for Production/Operations areas. My main focus
 is on designing and developing innovative solutions using Python, with a special interest in
 building robust and efficient applications to optimize processes and solve complex problems.
 Currently at Rappi, I am actively involved in Data Engineering and Python Development projects,
 leveraging my advanced knowledge in SQL, Python, FastAPI, Apache Airflow, and Snowflake.
"""

ABOUT_ME = cond(
    MainState.is_language_en,
    ENGLISH_ABOUT_ME,
    SPANISH_ABOUT_ME,
)
