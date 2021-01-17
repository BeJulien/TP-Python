# coding: utf-8

from types import SimpleNamespace

from . import OSRMError

from .types import create_maneuver
from .types import create_route
from .types import create_step

from .types.route import Route


class OSRMParserError(OSRMError):
    """
    Classe pour les erreurs liées au parser du module OSRM.
    """
    pass


class Parser:
    """
    Analyseur d'un itinéraire lié à une structure dynamique,
    celle-ci étant générée à partir d'un fichier au format JSON.

    Attributes:
        geo_data (SimpleNamespace): Les données de l'itinéraire à analyser.
    """

    def __init__(self, geo_data: SimpleNamespace):
        self.geo_data = geo_data

    def shortest_route(self) -> Route:
        """
        Analyse la structure contenant l'itinéraire pour créer une route.

        Returns:
            Une route contenant toutes les étapes de parcours.
        """
        if self.geo_data.code != "Ok" or not self.geo_data.routes[0]:
            raise OSRMParserError()

        route = self.geo_data.routes[0]

        steps = list()
        for step in route.legs[0].steps:
            maneuver = create_maneuver(step.maneuver)
            steps.append(create_step(step, maneuver))

        return create_route(route, steps)
