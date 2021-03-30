from fastapi import APIRouter
from domain.connpass2 import Factory, Connpass
import os
from model.event import Event
router = APIRouter()
apipath = "/api/v01"


@router.post(f"{apipath}/connpass")
def get_connpass(data: Event):
    com = Connpass()
    url, count = com.convert(data)
    return com.get(url, count)
