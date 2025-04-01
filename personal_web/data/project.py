import json

from pydantic import BaseModel, Field


class Project(BaseModel):
    name: str
    description: str
    technologies: list[str] = []
    repository_url: str = Field(
        default="/",
    )
    website_url: str = Field(default="/")


with open("assets/data/sp/projects.json", encoding="utf-8") as file:
    projects_data = json.load(file)

with open("assets/data/en/projects.json", encoding="utf-8") as file:
    projects_data_en = json.load(file)

projects_list: list[Project] = [Project(**item) for item in projects_data]
projects_en_list: list[Project] = [Project(**item) for item in projects_data_en]
