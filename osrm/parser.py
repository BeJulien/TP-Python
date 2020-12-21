# coding: utf-8

from types import SimpleNamespace

from .types import create_maneuver
from .types import create_route
from .types import create_step
from .types.route import Route


class Parser:
    def __init__(self, geo_data: SimpleNamespace):
        self.geo_data = geo_data

    def shortest_route(self) -> Route:
        route = self.geo_data.routes[0]

        steps = list()
        for step in route.legs[0].steps:
            maneuver = create_maneuver(step.maneuver)
            steps.append(create_step(step, maneuver))

        return create_route(route, steps)
