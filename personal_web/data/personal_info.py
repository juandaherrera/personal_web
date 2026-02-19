from reflex import cond

from personal_web.state import MainState
from personal_web.utils import get_experience

SPANISH_ABOUT_ME = f"""
Soy Ingeniero Industrial y Senior ML Backend Engineer con más de {get_experience()} años
de experiencia en backend y data engineering. Me enfoco en diseñar y evolucionar
sistemas distribuidos orientados a ML, priorizando escalabilidad, resiliencia y
excelencia operativa. Actualmente trabajo en Snoonu, donde soy responsable técnico
de servicios core construidos con Python y FastAPI, integrando modelos de ML en
arquitecturas de microservicios y asegurando alto rendimiento en producción.
También tengo experiencia en pipelines de datos y arquitecturas analíticas con
Airflow y Snowflake.
"""


ENGLISH_ABOUT_ME = f"""
I'm an Industrial Engineer and Senior ML Backend Engineer with over
{get_experience()} years of experience in backend and data engineering. I focus on
designing and evolving ML-oriented distributed systems, prioritizing scalability,
resilience, and operational excellence. Currently at Snoonu, I act as technical
owner of core services built with Python and FastAPI, integrating ML models into
scalable microservice architectures and ensuring strong production performance.
I also have experience building data pipelines and analytical architectures using
Airflow and Snowflake.
"""


ABOUT_ME = cond(
    MainState.is_language_en,
    ENGLISH_ABOUT_ME,
    SPANISH_ABOUT_ME,
)
