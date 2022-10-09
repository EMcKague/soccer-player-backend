import numbers
from typing import List
from pydantic import BaseModel

class Player(BaseModel):
    id: int
    name: str
    nationality: str
    national_position: str
    club: str
    height: int
    preffered_foot: str

    @classmethod
    def index(cls) -> List["Player"]:
        return [
            Player(id=1, name='test', nationality='NA', national_position='LF', club='Unknown', height=167, preffered_foot='right')
        ]