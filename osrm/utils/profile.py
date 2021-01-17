# coding: utf-8

from enum import Enum
from enum import unique


@unique
class Profile(Enum):
    CAR = "car"
    BIKE = "bike"
    FOOT = "foot"

    def __str__(self) -> str:
        return self.value
