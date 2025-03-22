import json

from pydantic import BaseModel


class Degree(BaseModel):
    title: str
    college: str
    college_logo: str
    start_year: int
    end_year: int

    @property
    def period(self):
        if self.start_year == self.end_year:
            return self.start_year
        return f"{self.start_year} - {self.end_year}"


with open("assets/data/sp/education.json", encoding="utf-8") as file:
    education_data = json.load(file)

with open("assets/data/en/education.json", encoding="utf-8") as file:
    education_data_en = json.load(file)


education_list: list[Degree] = [Degree(**item) for item in education_data]
education_en_list: list[Degree] = [Degree(**item) for item in education_data_en]
