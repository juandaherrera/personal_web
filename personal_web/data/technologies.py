import json

from pydantic import BaseModel


# TO_DO agregar Redash, Snowflake y PowerBI
class Technology(BaseModel):
    name: str
    icon: str
    url: str | None = "/"


with open("assets/data/technologies.json", encoding="utf-8") as file:
    tech_data = json.load(file)

tech_list: list[Technology] = [Technology(**item) for item in tech_data]
