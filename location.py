import json
import urllib.request
import requests
import os


class ApiLocation:

    def __init__(self):
        self.url = "http://api.ipstack.com/"
        self.ip = self.get_ip()
        self.connector = "?access_key="
        self.key = os.environ.get("LOCATION_API_KEY")
        self.location = self.city

    def get_ip(self):
       return urllib.request.urlopen('https://ident.me').read().decode('utf8')


    def get(self):
        return requests.get(self.url + self.ip + self.connector + self.key)

    def city(self):
        data = json.loads(self.get().text)
        return data["city"]


# here = ApiLocation()
#
#
# print(here.location())
