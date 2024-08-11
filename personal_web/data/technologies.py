import json
from typing import List, Optional

from pydantic import BaseModel


# TO_DO agregar Redash, Snowflake y PowerBI
class Technology(BaseModel):
    name: str
    icon: str
    url: Optional[str] = "/"


with open("assets/data/technologies.json") as file:
    tech_data = json.load(file)

tech_list: List[Technology] = [Technology(**item) for item in tech_data]
