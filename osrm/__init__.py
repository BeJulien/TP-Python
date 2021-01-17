# coding: utf-8

from configparser import ConfigParser
from typing import List
from typing import Tuple

from os.path import join

__author__ = "Julien Benac"

# Le chemin vers le fichier de configuration de l'API OSRM.
CONFIG_PATH = join("osrm", "config.ini")

# Le mode DEBUG sert à afficher ou non des informations utiles à
# la recherche d'erreurs. Si ce mode est activé, l'affichage des
# objects permettant d'identifier un itinéraire sera détaillé.
DEBUG = False


class OSRMError(Exception):
    """
    Classe de base pour les erreurs liées au module OSRM.
    """
    pass


def find_uri() -> str:
    """
    Récupère l'URI à utiliser pour le calcul d'itinéraire.

    Returns:
        L'URI à utiliser pour l'API OSRM.
    """
    parser = ConfigParser()
    parser.read(CONFIG_PATH)

    return parser.get("osrm-global", "uri")


def find_config() -> List[Tuple[str, str]]:
    """
    Récupère la configuration OSRM utilisée pour le calcul d'itinéraire.

    Returns:
        Une liste contenant les options de l'API OSRM.
    """
    parser = ConfigParser()
    parser.read(CONFIG_PATH)

    return parser.items("osrm-options")
