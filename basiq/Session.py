import requests
import time
from .API import API
from .services import UserService

class Session:
    def __init__(self, api, api_key):
        self.__api_key = api_key
        self.validity = None
        self.refreshed = None
        self.__token = None
        self.headers = None
        self.api = api

        self.get_token()

    def get_token(self):
        if self.validity != None and time.gmtime() - self.refreshed < self.validity:
            return self.__token

        r = self.api.set_header("Authorization", "Basic " + self.__api_key) \
                .set_header("basiq-version", "1.0") \
                .post("token", {})

        if "access_token" in r:
            self.refreshed = time.gmtime()
            self.validity = r["expires_in"]
            self.__token = r["access_token"]
            self.api.headers = {
                "Authorization": "Bearer " + r["access_token"]
            }
            return r["access_token"]
        else:
            print("No access token:", r)

    def get_institutions(self):
        return self.api.get("institutions")

    def get_institution(self, id):
        return self.api.get("institutions/" + id)

    def get_user(self, id):
        return UserService(self).get(id)

    def for_user(self, id):
        return UserService(self).forUser(id)

