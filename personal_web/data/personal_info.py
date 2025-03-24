from reflex import cond

from personal_web.state import MainState
from personal_web.utils import get_experience

SPANISH_ABOUT_ME = f"""
Soy Ingeniero Industrial y ML Backend Engineer con más de {get_experience()} años de experiencia
 en desarrollo backend e ingeniería de datos. Mi principal enfoque es construir y optimizar
 microservicios, garantizando escalabilidad, rendimiento y eficiencia en el manejo de datos.
 Actualmente, trabajo en Snoonu desarrollando soluciones backend utilizando Python, FastAPI,
 PostgreSQL y Redis, aplicando principios de código limpio, realizando pruebas con Pytest y
 automatizando flujos de trabajo con GitHub Actions. También tengo experiencia con Airflow y
 Snowflake, especialmente en entornos de ingeniería de datos.
"""

ENGLISH_ABOUT_ME = f"""
I'm an Industrial Engineer and ML Backend Engineer with over {get_experience()} years of experience
 in backend development and data engineering. My main focus is building and optimizing
 microservices, ensuring scalability, performance, and efficiency in data handling. Currently,
 I work at Snoonu, developing backend solutions using Python, FastAPI, PostgreSQL, and Redis, while
 applying clean code principles, testing with Pytest, and automating workflows with GitHub Actions.
 I also have experience with Airflow and Snowflake, particularly in Data Engineering environments.
"""

ABOUT_ME = cond(
    MainState.is_language_en,
    ENGLISH_ABOUT_ME,
    SPANISH_ABOUT_ME,
)
