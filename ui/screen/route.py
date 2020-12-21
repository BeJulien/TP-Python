# coding: utf-8

from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView

from kivymd.uix.screen import MDScreen

from osrm.router import Router

from .step import StepWidget
from .menu import MenuWidget

from ..utils import get_information_image


class RouteScreen(MDScreen):
    def calculation(self) -> None:
        search_screen = self.parent.get_screen("search_screen")

        router = Router(search_screen.lat_a, search_screen.lon_a, search_screen.lat_b, search_screen.lon_b)

        shortest_route = router.shortest_route()

        grid = GridLayout(cols=1, spacing=20, padding=20, size_hint_y=None)
        grid.bind(minimum_height=grid.setter("height"))

        scroll = ScrollView()
        scroll.add_widget(grid)

        if shortest_route.get_distance() >= 1000.0:
            distance = str(shortest_route.get_distance() / 1000.0) + " km"
        else:
            distance = str(shortest_route.get_distance()) + " m"
        grid.add_widget(MenuWidget(total_distance=distance))

        for step in shortest_route.get_steps():
            maneuver = step.get_maneuver()
            image_source = get_information_image(maneuver.get_modifier(), maneuver.get_type())

            if step.get_distance() >= 1000.0:
                distance = str(step.get_distance() / 1000.0) + " km"
            else:
                distance = str(step.get_distance()) + " m"

            grid.add_widget(StepWidget(image_source=image_source,
                                       name=step.get_name(),
                                       distance=distance))

        self.add_widget(scroll)

    def delete_scroll(self):
        self.remove_widget(self.children[0])
