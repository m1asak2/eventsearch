from typing import List, Optional
from datetime import datetime
from model.bases import Bases
from typing import List
from pydantic import BaseModel


class Event(BaseModel):
    keyword: List[str]
    address: List[str]
    start_from: str
    start_to: str
    limit: int


class EventTable(BaseModel):
    day: str
    time: str
    address: str
    title: str
    group: str
    img: str
    link: str
