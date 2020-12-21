# coding: utf-8

from enum import Enum
from enum import unique


@unique
class Version(Enum):
    V1 = "v1"

    def __str__(self) -> str:
        return self.value
