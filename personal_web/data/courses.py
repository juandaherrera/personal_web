import json
from datetime import date
from typing import List, Optional

from pydantic import BaseModel, validator


class Course(BaseModel):
    name: str
    issue_date: date
    credential_url: Optional[str]
    technologies: Optional[List[str]] = []

    @validator('technologies', pre=True, allow_reuse=True)
    def technologies_unicity(cls, v):
        return list(dict().fromkeys(v).keys())

    @property
    def issue_date_format(self):
        return self.issue_date.strftime('%b. %Y')


class School(BaseModel):
    name: str
    logo: str
    url: Optional[str]
    courses: List[Course]

    def __init__(self, **data):
        super().__init__(**data)
        self.courses = sorted(self.courses, key=lambda course: course.issue_date, reverse=True)

    @property
    def courses_qty(self):
        return len(self.courses)

    @property
    def last_course_at(self):
        return self.courses[0].issue_date


with open("assets/data/sp/courses.json") as file:
    schools_data = json.load(file)

with open("assets/data/en/courses.json") as file:
    schools_data_en = json.load(file)

schools_list: List[School] = [School(**item) for item in schools_data]
schools_list: List[School] = sorted(
    schools_list, key=lambda school: school.last_course_at, reverse=True
)

schools_en_list: List[School] = [School(**item) for item in schools_data_en]
schools_en_list: List[School] = sorted(
    schools_en_list, key=lambda school: school.last_course_at, reverse=True
)
