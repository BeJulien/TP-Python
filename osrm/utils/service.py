# coding: utf-8

from enum import Enum
from enum import unique


@unique
class Service(Enum):
    ROUTE = "route"
    NEAREST = "nearest"
    TABLE = "table"
    MATCH = "match"
    TRIP = "trip"
    TILE = "tile"

    def __str__(self) -> str:
        return self.value
