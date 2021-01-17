# coding: utf-8

from os.path import dirname
from os.path import join


def get_information_image(modifier: str, maneuver_type: str) -> str:
    """
    Récupère l'image à afficher en fonction de certains paramètres
    définis dans la définition d'une étape.

    Parameters:
        modifier: La direction à prendre lors de la prochaine intersection.
        maneuver_type: Le type de l'étape (départ ou intermédiaire).

    Returns:
        Le chemin vers l'image à afficher.
    """
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
        "depart": "depart",
    }

    image = types.get(maneuver_type) if maneuver_type in types.keys() else modifiers.get(modifier)

    return join(dirname(__file__), "screen", "img", f"{image}.png")


def format_distance(distance: float) -> str:
    """
    Formate une distance en fonction de la longueur pour proposer
    une chaîne de caractères lisible (arrondi, conversion).

    Parameters:
        distance: La distance à formater.

    Returns:
        La distance formatée, au mètre ou kilomètre près.
    """
    return f"{distance:.0f}m" if distance < 1000.0 else f"{(distance / 1000.0):.0f}km"
