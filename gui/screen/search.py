# coding: utf-8

from plyer import gps

from kivy.clock import mainthread
from kivy.properties import NumericProperty
from kivy.utils import platform

from kivymd.uix.screen import MDScreen
from kivymd.uix.snackbar import Snackbar

from mobile import request_android_permissions

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

    def on_enter(self) -> None:
        if platform == "android":
            request_android_permissions()

        try:
            gps.configure(on_location=self.on_location)
        except NotImplementedError:
            return

        gps.start(5000, 0)

    def on_leave(self) -> None:
        gps.stop()

    @mainthread
    def on_location(self, **kwargs) -> None:
        self.lat_a, self.lon_a = kwargs["lat"], kwargs["lon"]

        self.ids.get("current_location").text = get_address(self.lat_a, self.lon_a)

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
                Snackbar(text="L'adresse décrite n'est pas dans la même ville.").show()
        except NominatimSearchError or NominatimReverseError:
            Snackbar(text="L'adresse décrite n'est pas valide.").show()
