# coding: utf-8

from types import SimpleNamespace
from typing import List

from .maneuver import Maneuver
from .route import Route
from .step import Step

__author__ = "Julien Benac"

# La valeur par défaut pour les attributs de type chaîne de caractère.
DEFAULT_STR = str()

# La valeur par défaut pour les attributs de type entier.
DEFAULT_INT = int()

# La valeur par défaut pour les attributs de type flottant.
DEFAULT_FLOAT = float()


def create_route(r: SimpleNamespace, steps: List[Step]) -> Route:
    """
    Création d'un nouveau trajet à partir d'un namespace représentant un
    trajet. Si certains attributs ne sont pas présents dans le namespace,
    une valeur par défaut est affectée à la valeur correspondante.

    Parameters:
        r: Le namespace contenant les informations du trajet.
        steps: La liste des étapes de parcours pour le trajet.

    Returns:
        Un nouveau trajet entre deux points GPS.
    """
    n_distance = getattr(r, "distance", DEFAULT_FLOAT)
    n_duration = getattr(r, "duration", DEFAULT_FLOAT)

    return Route(n_distance, n_duration, steps)


def create_step(s: SimpleNamespace, m: Maneuver) -> Step:
    """
    Création d'une nouvelle étape de parcours à partir d'un namespace
    représentant une étape de parcours. Si certains attributs ne sont
    pas présents dans le namespace, une valeur par défaut est affectée
    à la valeur correspondante.

    Parameters:
        s: Le namespace contenant les informations de l'étape de parcours.
        m: La manoeuvre correspondant à l'étape de parcours.

    Returns:
        Une nouvelle étape de parcours avec les informations voulues.
    """
    n_distance = getattr(s, "distance", DEFAULT_FLOAT)
    n_duration = getattr(s, "duration", DEFAULT_FLOAT)
    n_name = getattr(s, "name", DEFAULT_STR)
    n_ref = getattr(s, "ref", DEFAULT_STR)

    return Step(n_distance, n_duration, n_name, n_ref, m)


def create_maneuver(m: SimpleNamespace) -> Maneuver:
    """
    Création d'une nouvelle manoeuvre à partir d'un namespace représentant une
    manoeuvre. Si certains attributs ne sont pas présents dans le namespace,
    une valeur par défaut est affectée à la valeur correspondante.

    Parameters:
        m: Le namespace contenant les informations de la manoeuvre.

    Returns:
        Une nouvelle manoeuvre avec les informations voulues.
    """
    n_bearing_before = getattr(m, "bearing_before", DEFAULT_INT)
    n_bearing_after = getattr(m, "bearing_after", DEFAULT_INT)
    n_type = getattr(m, "type", DEFAULT_STR)
    n_modifier = getattr(m, "modifier", DEFAULT_STR)
    n_exit = getattr(m, "exit", DEFAULT_INT)

    return Maneuver(n_bearing_before, n_bearing_after, n_type, n_modifier, n_exit)
