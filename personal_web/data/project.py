import json
from typing import List, Optional

from pydantic import AnyUrl, BaseModel


class Project(BaseModel):
    name: str
    description: str
    technologies: List[str] = []
    repository_url: Optional[AnyUrl]
    website_url: Optional[AnyUrl] = "/"


with open("assets/data/projects.json") as file:
    projects_data = json.load(file)

projects_list: List[Project] = [Project(**item) for item in projects_data]
