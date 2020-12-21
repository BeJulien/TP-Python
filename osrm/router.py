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
    pass


class Router:
    def __init__(self, lat_a: float, lon_a: float, lat_b: float, lon_b: float):
        self.lat_a = lat_a
        self.lon_a = lon_a
        self.lat_b = lat_b
        self.lon_b = lon_b

    def shortest_route(self) -> Route:
        request = requests.get(f"{find_uri()}/{Service.ROUTE}/{Version.V1}/{Profile.FOOT}/"
                               f"{self.lon_a},{self.lat_a};{self.lon_b},{self.lat_b}", params=find_config())
        response = json.loads(request.text, object_hook=lambda d: SimpleNamespace(**d))

        if request.status_code != HTTPStatus.OK or not response:
            raise OSRMRouterError()

        parser = Parser(response)

        return parser.shortest_route()
