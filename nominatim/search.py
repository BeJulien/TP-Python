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
    """
    Classe pour les erreurs liées au search du module Nominatim.
    """
    pass


def get_location(address: str) -> Tuple[float, float]:
    """
    Récupère les coordonnées à partir de l'adresse.

    Parameters:
        address: L'adresse des coordonnées recherchées.

    Returns:
        Les coordonnées déduites de l'adresse.
    """
    request = requests.get(f"{find_uri()}{SEARCH_PATH}?q={address}", params=find_config())
    response = json.loads(request.text)

    if request.status_code != HTTPStatus.OK or not response:
        raise NominatimSearchError()

    return response[0].get("lat"), response[0].get("lon")


def get_osm_type(address: str) -> str:
    """
    Récupère le type OpenStreetMap (OSM) à partir de l'adresse.

    Parameters:
        address: L'adresse des coordonnées recherchées.

    Returns:
        Le type OpenStreetMap (OSM).
    """
    request = requests.get(f"{find_uri()}{SEARCH_PATH}?q={address}", params=find_config())
    response = json.loads(request.text)

    if request.status_code != HTTPStatus.OK or not response:
        raise NominatimSearchError()

    osm_type = response[0].get("osm_type")

    return "N" if osm_type == "node" else ("W" if osm_type == "way" else "R")


def get_osm_id(address: str) -> int:
    """
    Récupère l'identifiant OpenStreetMap (OSM) à partir de l'adresse.

    Parameters:
        address: L'adresse des coordonnées recherchées.

    Returns:
        L'identifiant OpenStreetMap (OSM).
    """
    request = requests.get(f"{find_uri()}{SEARCH_PATH}?q={address}", params=find_config())
    response = json.loads(request.text)

    if request.status_code != HTTPStatus.OK or not response:
        raise NominatimSearchError()

    return response[0].get("osm_id")
