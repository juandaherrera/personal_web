import json
from datetime import date
from typing import List, Optional, Union

from pydantic import AnyUrl, BaseModel, validator


class Job(BaseModel):
    title: str
    start_date: date
    end_date: Union[date, str]
    company_name: str
    company_url: Optional[AnyUrl]
    company_logo: Optional[str]
    description: str
    achievements: Optional[str]

    # TO_DO podría agregar Babel para enviar las fechas en español.
    @property
    def start_date_format(self):
        return self.start_date.strftime('%b. %Y') if self.start_date else None

    @property
    def end_date_format(self):
        return (
            'actualidad'
            if str(self.end_date).isalpha()
            else self.end_date.strftime('%b. %Y')
        )

    # TO_DO Lógica para calcular el tiempo en cada posición. Ideal que la actual se recalcule cada día.
    @property
    def time(self):
        if str(self.end_date).isalpha():
            return None


with open("assets/data/work_experience.json") as file:
    work_data = json.load(file)

work_experience_list: List[Job] = [Job(**item) for item in work_data]
