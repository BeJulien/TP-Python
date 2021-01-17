# coding: utf-8

from dataclasses import dataclass
from dataclasses import field

from osrm import DEBUG


@dataclass(repr=DEBUG)
class Maneuver:
    bearing_before: int = field(default_factory=int)
    bearing_after: int = field(default_factory=int)
    type: str = field(default_factory=str)
    modifier: str = field(default_factory=str)
    exit: int = field(default_factory=int)

    def get_bearing_before(self) -> int:
        return self.bearing_before

    def get_bearing_after(self) -> int:
        return self.bearing_after

    def get_type(self) -> str:
        return self.type

    def get_modifier(self) -> str:
        return self.modifier

    def get_exit(self) -> int:
        return self.exit
