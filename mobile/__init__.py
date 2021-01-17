# coding: utf-8

from android.permissions import Permission
from android.permissions import request_permissions

__author__ = "Julien Benac"


def request_android_permissions() -> None:
    request_permissions([
        Permission.INTERNET,
        Permission.ACCESS_COARSE_LOCATION,
        Permission.ACCESS_FINE_LOCATION
    ])
