import json

from pydantic import BaseModel


class Certification(BaseModel):
    title: str
    institute: str
    institute_logo: str
    start_year: int
    end_year: int
    credential_url: str | None = "/"

    @property
    def period(self):
        if self.start_year == self.end_year:
            return self.start_year
        return f"{self.start_year} - {self.end_year}"


with open("assets/data/sp/certifications.json", encoding="utf-8") as file:
    certifications_data = json.load(file)

with open("assets/data/en/certifications.json", encoding="utf-8") as file:
    certifications_data_en = json.load(file)

certifications_list: list[Certification] = [Certification(**item) for item in certifications_data]
certifications_en_list: list[Certification] = [
    Certification(**item) for item in certifications_data_en
]
