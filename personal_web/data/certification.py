import json
from typing import List, Optional

from pydantic import AnyUrl, BaseModel


class Certification(BaseModel):
    title: str
    institute: str
    institute_logo: str
    start_year: int
    end_year: int
    credential_url: Optional[AnyUrl] = '/'

    @property
    def period(self):
        if self.start_year == self.end_year:
            return self.start_year
        return f"{self.start_year} - {self.end_year}"


with open("assets/data/certifications.json") as file:
    certifications_data = json.load(file)

certifications_list: List[Certification] = [
    Certification(**item) for item in certifications_data
]
