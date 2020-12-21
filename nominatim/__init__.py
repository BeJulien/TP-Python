# coding: utf-8

from configparser import ConfigParser
from typing import List
from typing import Tuple

from os.path import join

__author__ = "Julien Benac"

CONFIG_PATH = join("nominatim", "config.ini")


class NominatimError(Exception):
    pass


def find_uri() -> str:
    parser = ConfigParser()
    parser.read(CONFIG_PATH)

    return parser.get("nominatim-global", "uri")


def find_config() -> List[Tuple[str, str]]:
    parser = ConfigParser()
    parser.read(CONFIG_PATH)

    return parser.items("nominatim-options")
