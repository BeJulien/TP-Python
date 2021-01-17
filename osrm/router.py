# coding: utf-8

import json
import requests

from http import HTTPStatus
from types import SimpleNamespace

from . import OSRMError
from . import find_config
from . import find_uri

from .parser import Parser

from .types.route import Route
from .utils.profile import Profile
from .utils.service import Service
from .utils.version import Version


class OSRMRouterError(OSRMError):
    """
    Classe pour les erreurs liées au router du module OSRM.
    """
    pass


class Router:
    """
    Calculateur d'un itinéraire entre deux points définis. Attention, aucune
    vérification  n'est effectuée à l'intérieur de celle-ci, les deux points
    peuvent donc être dans des villes différentes.

    Attributes:
        lat_a (float): La latitude du point de départ.
        lon_a (float): La longitude du point de départ.
        lat_b (float): La latitude du point d'arrivée.
        lon_b (float): La longitude du point d'arrivée.
    """

    def __init__(self, lat_a: float, lon_a: float, lat_b: float, lon_b: float):
        self.lat_a = lat_a
        self.lon_a = lon_a
        self.lat_b = lat_b
        self.lon_b = lon_b

    def shortest_route(self) -> Route:
        """
        Récupère l'itinéraire le plus court en utilisant l'API OSRM.

        Returns:
            Une route contenant toutes les étapes de parcours.
        """
        request = requests.get(f"{find_uri()}/{Service.ROUTE}/{Version.V1}/{Profile.FOOT}/"
                               f"{self.lon_a},{self.lat_a};{self.lon_b},{self.lat_b}", params=find_config())
        response = json.loads(request.text, object_hook=lambda d: SimpleNamespace(**d))

        if request.status_code != HTTPStatus.OK or not response:
            raise OSRMRouterError()

        parser = Parser(response)

        return parser.shortest_route()
