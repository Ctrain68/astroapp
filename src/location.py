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
    ''' Method to find the users public IP address'''

    def get_ip(self):
        return urllib.request.urlopen('https://ident.me').read().decode('utf8')

    ''' Method to return JSON data for Public IP Address from API'''

    def get(self):
        return requests.get(self.url + self.ip + self.connector + self.key)
    '''Method for converting JSON data and
    returning city from API based on Public IP Adress'''

    def city(self) -> dict:
        data = json.loads(self.get().text)
        return data["city"]
