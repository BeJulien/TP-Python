# coding: utf-8

from kivy.clock import Clock
from kivy.properties import NumericProperty

from kivymd.uix.screen import MDScreen
from kivymd.uix.snackbar import Snackbar

from nominatim.lookup import is_same_town
from nominatim.reverse import NominatimReverseError
from nominatim.reverse import get_address
from nominatim.search import NominatimSearchError
from nominatim.search import get_location


class SearchScreen(MDScreen):
    lat_a = NumericProperty()
    lon_a = NumericProperty()
    lat_b = NumericProperty()
    lon_b = NumericProperty()

    def on_pre_enter(self):
        Clock.schedule_once(self.current_location)

    def current_location(self, callback: float) -> None:
        self.lat_a, self.lon_a = 44.360117, 2.575524  # Stub

        self.ids.get("current_location").text = "Votre adresse actuelle :\n" \
                                                f"{get_address(self.lat_a, self.lon_a)}"

    def verify_town(self) -> None:
        location_input = self.ids.get("location_input").text

        try:
            lat_b, lon_b = get_location(location_input)
            if is_same_town(self.lat_a, self.lon_a, lat_b, lon_b):
                self.lat_b = lat_b
                self.lon_b = lon_b

                self.parent.transition.direction = "left"
                self.parent.current = "route_screen"
            else:
                Snackbar(text="L'adresse décrite n'est pas dans la ville où vous êtes.").show()
        except NominatimSearchError or NominatimReverseError:
            Snackbar(text="L'adresse décrite n'est pas valide.").show()
