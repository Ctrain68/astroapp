from datetime import datetime 
import socket
import json
import urllib.request
import requests
from location import ApiLocation
from location import ApiMoon
import os
import time
from sys import stdout

greeting = "Welcome to ASTROAPP V1.0"





date_selected = input("Please enter the date you require data for in YYYY-MM-DD format.")


here = ApiLocation()


moons = ApiMoon()

print(moons.object_for_date())
 
print(moons.object_today())