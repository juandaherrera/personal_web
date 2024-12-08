import json
from datetime import date
from typing import List, Optional, Union

import reflex as rx
from pydantic import BaseModel, field_validator

from personal_web.utils import date_difference


class Job(BaseModel):
    title: str
    start_date: date
    end_date: Optional[date]
    description: str
    achievements: Optional[str]
    technologies: Optional[List[str]] = []

    @field_validator("technologies", mode="before")
    def technologies_unicity(cls, v):
        return list(dict.fromkeys(v))

    def get_duration(
        self, overwrite_end_date: Optional[date] = None, is_lang_en: bool = False
    ) -> str:
        if overwrite_end_date:
            return date_difference(self.start_date, overwrite_end_date, is_lang_en)
        return date_difference(self.start_date, self.end_date, is_lang_en)


class Company(BaseModel):
    company_name: str
    company_url: Optional[str]
    company_logo: Optional[str]
    jobs: List[Job]

    def __init__(self, **data):
        super().__init__(**data)
        self.sort_jobs()

    def sort_jobs(self):
        self.jobs.sort(key=lambda x: x.start_date, reverse=True)

    @property
    def start_date(self) -> date:
        return min(job.start_date for job in self.jobs)

    @property
    def end_date(self) -> Union[date, str]:
        try:
            return min(job.end_date for job in self.jobs)
        except TypeError:
            return date.today()

    @property
    def is_current_company(self) -> bool:
        return self.end_date == date.today()

    def get_duration(
        self, overwrite_end_date: Optional[date] = None, is_lang_en: bool = False
    ) -> str:
        if overwrite_end_date:
            return date_difference(self.start_date, overwrite_end_date, is_lang_en)
        return date_difference(self.start_date, self.end_date, is_lang_en)


class Resume(BaseModel):
    companies: Optional[List[Company]] = None

    def __init__(self, **data):
        super().__init__(**data)
        self.sort_companies()

    def sort_companies(self):
        if self.companies:
            self.companies.sort(key=lambda x: x.end_date, reverse=True)


# TODO just have one file with both languages
with open("assets/data/sp/work_experience.json", "r") as file:
    work_data = json.load(file)

with open("assets/data/en/work_experience.json", "r") as file:
    work_data_en = json.load(file)

resume = Resume(companies=work_data)
resume_en = Resume(companies=work_data_en)
