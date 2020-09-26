from datetime import datetime
import json
import urllib.request
import requests
import os
from dotenv import load_dotenv

# hostname = socket.gethostname()
# local_ip = socket.gethostbyname(hostname)

# print(local_ip)

# external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')

# print(external_ip)

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)

# LOCATION_API_KEY = os.environ.get("LOCATION_API_KEY")

class ApiLocation:
    



    def __init__(self):
        self.url = "http://api.ipstack.com/"
        self.ip = self.get_ip()
        self.connector = "?access_key="
        self.key = os.environ.get("LOCATION_API_KEY")
        self.location = self.city



    def get_ip(self):
        external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
        return external_ip

    
    def get(self):
        return requests.get(self.url+self.ip+self.connector+self.key)

    def city(self):
        data = json.loads(self.get().text)
        # print(json.loads(data.text))
        # print(f"This is your city {data['city']}")
        return data["city"]


here = ApiLocation()



print(here.location())





