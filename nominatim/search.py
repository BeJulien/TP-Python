# coding: utf-8

import json
import requests

from http import HTTPStatus
from typing import Tuple

from . import NominatimError
from . import find_config
from . import find_uri

SEARCH_PATH = "/search"


class NominatimSearchError(NominatimError):
    pass


def get_location(address: str) -> Tuple[float, float]:
    request = requests.get(f"{find_uri()}{SEARCH_PATH}?q={address}", params=find_config())
    response = json.loads(request.text)

    if request.status_code != HTTPStatus.OK or not response:
        raise NominatimSearchError()

    return response[0].get("lat"), response[0].get("lon")


def get_osm_type(address: str) -> str:
    request = requests.get(f"{find_uri()}{SEARCH_PATH}?q={address}", params=find_config())
    response = json.loads(request.text)

    if request.status_code != HTTPStatus.OK or not response:
        raise NominatimSearchError()

    osm_type = response[0].get("osm_type")

    return "N" if osm_type == "node" else ("W" if osm_type == "way" else "R")


def get_osm_id(address: str) -> int:
    request = requests.get(f"{find_uri()}{SEARCH_PATH}?q={address}", params=find_config())
    response = json.loads(request.text)

    if request.status_code != HTTPStatus.OK or not response:
        raise NominatimSearchError()

    return response[0].get("osm_id")
