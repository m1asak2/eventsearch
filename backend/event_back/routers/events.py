from fastapi import APIRouter
from domain.connpass2 import Connpass
from domain.Factory import Factory
from model.event import Event
router = APIRouter()
apipath = "/api/v01"


@router.post(f"{apipath}/connpass")
def get_connpass(data: Event):
    com = Connpass()
    return com.get_event(data)


@router.post(f"{apipath}/event")
def get_event(data: Event):
    res = []
    for target in data.target:
        com = Factory(target).strategy
        res += com.get_event(data)

    return res
