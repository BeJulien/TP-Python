# coding: utf-8

import json
import requests

from http import HTTPStatus

from . import NominatimError
from . import find_config
from . import find_uri

from nominatim.reverse import get_osm_id
from nominatim.reverse import get_osm_type

LOOKUP_PATH = "/lookup"


class NominatimLookupError(NominatimError):
    pass


def get_postcode(address_type: str, osm_id: int) -> str:
    request = requests.get(f"{find_uri()}{LOOKUP_PATH}?osm_ids={address_type}{osm_id}", params=find_config())
    response = json.loads(request.text)

    if request.status_code != HTTPStatus.OK or not response:
        raise NominatimLookupError()

    return response[0].get("address").get("postcode")


def is_same_town(lat_a: float, lon_a: float, lat_b: float, lon_b: float) -> bool:
    postcode_a = get_postcode(get_osm_type(lat_a, lon_a), get_osm_id(lat_a, lon_a))
    postcode_b = get_postcode(get_osm_type(lat_b, lon_b), get_osm_id(lat_b, lon_b))

    return postcode_a == postcode_b
