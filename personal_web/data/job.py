import json
from datetime import date, timedelta

from pydantic import BaseModel, Field, field_validator

from personal_web.utils import date_difference


class Job(BaseModel):
    title: str
    start_date: date
    end_date: date = Field(default_factory=lambda: date.today() + timedelta(days=365))
    description: str
    achievements: str | None
    technologies: list[str] = Field(default_factory=list)

    @field_validator("technologies", mode="before")
    @classmethod
    def technologies_unicity(cls, v):
        return list(dict.fromkeys(v))

    @field_validator("end_date", mode="before")
    @classmethod
    def validate_dates(cls, v):
        return date.today() + timedelta(days=365) if not v else v

    def get_duration(
        self, overwrite_end_date: date | None = None, is_lang_en: bool = False
    ) -> str:
        if overwrite_end_date:
            return date_difference(self.start_date, overwrite_end_date, is_lang_en)
        return date_difference(self.start_date, self.end_date, is_lang_en)


class Company(BaseModel):
    company_name: str
    company_url: str | None
    company_logo: str | None
    jobs: list[Job]

    def __init__(self, **data):
        super().__init__(**data)
        self.sort_jobs()

    def sort_jobs(self):
        self.jobs.sort(key=lambda x: x.start_date, reverse=True)

    @property
    def start_date(self) -> date:
        return min(job.start_date for job in self.jobs)

    @property
    def end_date(self) -> date:
        try:
            return max(job.end_date for job in self.jobs)
        except TypeError:
            return date.today()

    @property
    def is_current_company(self) -> bool:
        return self.end_date == date.today()

    def get_duration(
        self, overwrite_end_date: date | None = None, is_lang_en: bool = False
    ) -> str:
        if overwrite_end_date:
            return date_difference(self.start_date, overwrite_end_date, is_lang_en)
        return date_difference(self.start_date, self.end_date, is_lang_en)


class Resume(BaseModel):
    companies: list[Company] = Field(default_factory=list)

    def __init__(self, **data):
        super().__init__(**data)
        self.sort_companies()

    def sort_companies(self):
        if self.companies:
            self.companies.sort(key=lambda x: x.end_date, reverse=True)


# TODO(@juandaherrera): just have one file with both languages
with open("assets/data/sp/work_experience.json", encoding="utf-8") as file:
    work_data = json.load(file)

with open("assets/data/en/work_experience.json", encoding="utf-8") as file:
    work_data_en = json.load(file)

resume = Resume(companies=work_data)
resume_en = Resume(companies=work_data_en)
