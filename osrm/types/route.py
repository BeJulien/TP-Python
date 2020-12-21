# coding: utf-8

from dataclasses import dataclass
from dataclasses import field
from typing import List

from osrm import DEBUG
from osrm.types.step import Step


@dataclass(repr=DEBUG)
class Route:
    distance: float = field(default_factory=float)
    duration: float = field(default_factory=float)
    steps: List[Step] = field(default_factory=list)

    def get_distance(self) -> float:
        return self.distance

    def get_duration(self) -> float:
        return self.duration

    def get_steps(self) -> List[Step]:
        return self.steps
