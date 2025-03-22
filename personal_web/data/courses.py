import json
from datetime import date

from pydantic import BaseModel, Field, validator


class Course(BaseModel):
    name: str
    issue_date: date
    credential_url: str | None
    technologies: list[str] = Field(default=[])

    @validator("technologies", pre=True, allow_reuse=True)
    @classmethod
    def technologies_unicity(cls, v):
        return list(dict().fromkeys(v).keys())

    @property
    def issue_date_format(self):
        return self.issue_date.strftime("%b. %Y")


class School(BaseModel):
    name: str
    logo: str
    url: str | None
    courses: list[Course]

    def __init__(self, **data):
        super().__init__(**data)
        self.courses = sorted(self.courses, key=lambda course: course.issue_date, reverse=True)

    @property
    def courses_qty(self):
        return len(self.courses)

    @property
    def last_course_at(self):
        return self.courses[0].issue_date


with open("assets/data/sp/courses.json", encoding="utf-8") as file:
    schools_data = json.load(file)

with open("assets/data/en/courses.json", encoding="utf-8") as file:
    schools_data_en = json.load(file)

schools_list: list[School] = sorted(
    [School(**item) for item in schools_data],
    key=lambda school: school.last_course_at,
    reverse=True,
)

schools_en_list: list[School] = sorted(
    [School(**item) for item in schools_data_en],
    key=lambda school: school.last_course_at,
    reverse=True,
)
