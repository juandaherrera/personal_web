import json
from datetime import date
from typing import List, Optional, Union

from dateutil.relativedelta import relativedelta
from pydantic import BaseModel, validator

from personal_web.state import MainState


class Job(BaseModel):
    title: str
    start_date: date
    end_date: Union[date, str]
    company_name: str
    company_url: Optional[str]
    company_logo: Optional[str]
    description: str
    achievements: Optional[str]
    technologies: Optional[List[str]] = []

    @validator('technologies', pre=True, allow_reuse=True)
    def technologies_unicity(cls, v):
        return list(dict().fromkeys(v).keys())

    # TO_DO podría agregar Babel para enviar las fechas en español.
    @property
    def start_date_format(self):
        return (
            self.start_date.strftime('%b. %Y')
            if self.start_date and isinstance(self.start_date, date)
            else None
        )

    @property
    def end_date_format(self):
        if self.end_date == "":
            return 'actualidad'
        try:
            return self.end_date.strftime('%b. %Y')
        except:
            return date.fromisoformat(self.end_date).strftime('%b. %Y')

    @property
    def is_current_job(self):
        return isinstance(self.end_date, str)

    def calculate_duration(self):
        if isinstance(self.end_date, str):
            end_date = date.today()
        else:
            end_date = self.end_date

        # Para igualar el calculo de LinkedIn
        end_date = end_date + relativedelta(months=+1)

        # Calcula la diferencia entre las fechas
        diff = relativedelta(end_date, self.start_date)
        years = diff.years
        months = diff.months

        # Formatea la salida según la duración
        if years == 0 and months <= 1:
            return "1 mes"
        elif years == 0:
            return f"{months} meses"
        elif years == 1 and months == 1:
            return f"1 año y 1 mes"
        elif years == 1:
            return f"1 año y {months} meses" if months else "1 año"
        elif months == 1:
            return f"{years} años y 1 mes"
        else:
            return f"{years} años y {months} meses" if months else f"{years} años"


with open("assets/data/sp/work_experience.json", "r") as file:
    work_data = json.load(file)

with open("assets/data/en/work_experience.json", "r") as file:
    work_data_en = json.load(file)

work_experience_list: List[Job] = [Job(**item) for item in work_data]
work_experience_en_list: List[Job] = [Job(**item) for item in work_data_en]
