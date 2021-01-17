# coding: utf-8

from main import __version__

from osrm.router import Router

from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivymd.uix.screen import MDScreen
from kivymd.uix.toolbar import MDBottomAppBar
from kivymd.uix.toolbar import MDToolbar

from .step import StepWidget

from ..utils import format_distance
from ..utils import get_information_image


class RouteScreen(MDScreen):
    def calculation(self) -> None:
        """
        Calcule l'itinéraire le plus court entre deux points, une liste
        contenant toutes les étapes est mise en place ainsi qu'un bouton
        afin de supprimer l'itinéraire calculé.
        """
        search_screen = self.parent.get_screen("search_screen")

        router = Router(search_screen.lat_a, search_screen.lon_a, search_screen.lat_b, search_screen.lon_b)

        shortest_route = router.shortest_route()

        grid = GridLayout(cols=1, spacing=30, padding=(40, 40, 40, 160), size_hint_y=None)
        grid.bind(minimum_height=grid.setter("height"))

        scroll = ScrollView()
        scroll.add_widget(grid)

        for step in shortest_route.get_steps():
            maneuver = step.get_maneuver()
            image_source = get_information_image(maneuver.get_modifier(), maneuver.get_type())

            grid.add_widget(StepWidget(image_source=image_source,
                                       name=step.get_name(),
                                       distance=f"Marchez sur {format_distance(step.get_distance())}"))

        self.add_widget(scroll)

        bottom_bar = MDBottomAppBar()
        toolbar = MDToolbar(title=f"v{__version__}", type="bottom", icon="delete", icon_color=(1, 1, 1, 1))
        toolbar.on_action_button = self.delete_screen
        bottom_bar.add_widget(toolbar)

        self.add_widget(bottom_bar)

    def delete_screen(self) -> None:
        """
        Supprime tous les widgets créés sur l'écran d'affichage de
        l'itinéraire puis affiche l'écran de recherche.
        """
        while True:
            try:
                self.remove_widget(self.children[0])
            except IndexError:
                break  # Il n'y a plus de widgets à supprimer.

        self.parent.transition.direction = "right"
        self.parent.current = "search_screen"
