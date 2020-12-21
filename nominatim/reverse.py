# coding: utf-8

import json
import requests

from http import HTTPStatus

from . import NominatimError
from . import find_config
from . import find_uri

REVERSE_PATH = "/reverse"


class NominatimReverseError(NominatimError):
    pass


def get_address(lat: float, lon: float) -> str:
    request = requests.get(f"{find_uri()}{REVERSE_PATH}?lat={lat}&lon={lon}", params=find_config())
    response = json.loads(request.text)

    if request.status_code != HTTPStatus.OK or not response:
        raise NominatimReverseError()

    address = response.get("address")

    address_str = str()
    address_str += f"{address.get('house_number')} " if address.get("house_number") else str()
    address_str += f"{address.get('road')}, " if address.get("road") else str()
    address_str += f"{address.get('town')} " if address.get("town") else str()
    address_str += f"{address.get('postcode')}, " if address.get("postcode") else str()
    address_str += f"{address.get('country')} " if address.get("country") else str()

    return address_str


def get_osm_type(lat: float, lon: float) -> str:
    request = requests.get(f"{find_uri()}{REVERSE_PATH}?lat={lat}&lon={lon}", params=find_config())
    response = json.loads(request.text)

    if request.status_code != HTTPStatus.OK or not response:
        raise NominatimReverseError()

    osm_type = response.get("osm_type")

    return "N" if osm_type == "node" else ("W" if osm_type == "way" else "R")


def get_osm_id(lat: float, lon: float) -> int:
    request = requests.get(f"{find_uri()}{REVERSE_PATH}?lat={lat}&lon={lon}", params=find_config())
    response = json.loads(request.text)

    if request.status_code != HTTPStatus.OK or not response:
        raise NominatimReverseError()

    return response.get("osm_id")
