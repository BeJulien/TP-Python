# coding: utf-8

from configparser import ConfigParser
from typing import List
from typing import Tuple

from os.path import join

__author__ = "Julien Benac"

# Le chemin vers le fichier de configuration de l'API Nominatim.
CONFIG_PATH = join("nominatim", "config.ini")


class NominatimError(Exception):
    """
    Classe de base pour les erreurs liées au module Nominatim.
    """
    pass


def find_uri() -> str:
    """
    Récupère l'URI à utiliser pour utiliser des données OSM (OpenStreetMap).

    Returns:
        L'URI à utiliser pour l'API Nominatim.
    """
    parser = ConfigParser()
    parser.read(CONFIG_PATH)

    return parser.get("nominatim-global", "uri")


def find_config() -> List[Tuple[str, str]]:
    """
    Récupère la configuration Nominatim utilisée pour l'utilisation de données.

    Returns:
        Une liste contenant les options de l'API Nominatim.
    """
    parser = ConfigParser()
    parser.read(CONFIG_PATH)

    return parser.items("nominatim-options")
