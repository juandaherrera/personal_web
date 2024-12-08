import json
from typing import List, Optional

from pydantic import BaseModel


class Project(BaseModel):
    name: str
    description: str
    technologies: List[str] = []
    repository_url: Optional[str]
    website_url: Optional[str] = "/"


with open("assets/data/sp/projects.json", "r") as file:
    projects_data = json.load(file)

with open("assets/data/en/projects.json", "r") as file:
    projects_data_en = json.load(file)

projects_list: List[Project] = [Project(**item) for item in projects_data]
projects_en_list: List[Project] = [Project(**item) for item in projects_data_en]
