import reflex as rx

from personal_web.data.job import resume, resume_en
from personal_web.utils import date_difference

initial_company_list = [
    date_difference(company.start_date, company.end_date, False) for company in resume.companies
]
initial_job_list: list[list[str]] = [
    [date_difference(job.start_date, job.end_date, False) for job in company.jobs]
    for company in resume.companies
]


class MainState(rx.State):
    is_language_en: bool = False
    companies_duration: list[str] = initial_company_list
    jobs_duration: list[list[str]] = initial_job_list

    @rx.event
    def toggle_language(self):
        self.is_language_en = not self.is_language_en
        self.calculate_durations()

    @rx.event
    def calculate_durations(self):
        selected_obj = resume_en if self.is_language_en else resume
        self.companies_duration = [
            date_difference(company.start_date, company.end_date, self.is_language_en)
            for company in selected_obj.companies
        ]
        self.jobs_duration = [
            [
                date_difference(job.start_date, job.end_date, self.is_language_en)
                for job in company.jobs
            ]
            for company in selected_obj.companies
        ]
