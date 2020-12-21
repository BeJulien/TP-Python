# coding: utf-8

from os.path import dirname
from os.path import join


def get_information_image(modifier: str, maneuver_type: str) -> str:
    modifiers = {
        "": "none",
        "left": "left",
        "right": "right",
        "sharp left": "sharp-left",
        "sharp right": "sharp-right",
        "slight left": "slight-left",
        "slight right": "slight-right",
        "straight": "straight",
        "uturn": "uturn"
    }

    types = {
        "depart": "depart-arrive",
        "arrive": "depart-arrive"
    }

    image = types.get(maneuver_type) if maneuver_type in types.keys() else modifiers.get(modifier)

    return join(dirname(__file__), "screen", "img", f"{image}.png")
