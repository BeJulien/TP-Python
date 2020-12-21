# coding: utf-8

from dataclasses import dataclass
from dataclasses import field

from osrm import DEBUG
from osrm.types.maneuver import Maneuver


@dataclass(repr=DEBUG)
class Step:
    distance: float = field(default_factory=float)
    duration: float = field(default_factory=float)
    name: str = field(default_factory=str)
    ref: str = field(default_factory=str)
    maneuver: Maneuver = field(default_factory=Maneuver)

    def get_distance(self) -> float:
        return self.distance

    def get_duration(self) -> float:
        return self.duration

    def get_name(self) -> str:
        return self.name

    def get_ref(self) -> str:
        return self.ref

    def get_maneuver(self) -> Maneuver:
        return self.maneuver
