from datetime import date
from location import ApiLocation
import json
import requests
import os
from dotenv import load_dotenv

# MOON_API_KEY = os.environ.get("MOON_API_KEY")

location = ApiLocation()


class ApiMoon:
    def __init__(self):
        self.url = "https://api.ipgeolocation.io/astronomy?apiKey="
        self.key = os.environ.get("MOON_API_KEY")
        self.connector = "&location="
        self.location = location.city()
        self.date_connector = "&date="
        self.date_selected = self.get_date()
        self.any_date = self.for_date()
        self.sunrise = "Sunrise time is "
        self.sunset = " Sunset time is "
        self.moonrise = "Moonrise time is "
        self.moonset = " Mooonset time is "
        self.sun_combined = self.sunrise + str(self.any_date['sunrise']) + self.sunset + str(self.any_date["sunset"])
        self.moon_combined = self.moonrise + str(self.any_date['moonrise']) + self.moonset + str(
            self.any_date["moonset"])

    def get_date(self):
        enter_date = int(input("Please select 1 to use current date or 2 to enter in a date of your choice: "))
        while enter_date != 1 and enter_date != 2:
            enter_date = int(input("""Please select 1 to use current date or 2 to enter in a date of your choice: """))

        if enter_date == 1:
            today = date.today()

            todays_date = today.strftime("%Y-%m-%d")
            print(f"You have selected {todays_date} as your date")
            return todays_date

        elif enter_date == 2:
            year = input("Enter year: YYYY\n ")
            month = input("Enter Month:MM\n ")
            day = input("Enter Date:DD\n")
            other_date = f"{year}-{month}-{day}"
            print(f"You have selected {other_date} as your date")
            return other_date

    def get(self):
        # print(self.url+self.key+self.connector+self.location+self.date_connector+self.date_selected)
        return requests.get(
            self.url + self.key + self.connector + self.location + self.date_connector + self.date_selected)

    def for_date(self):

        return json.loads(self.get().text)

    def object_for_date(self):
        luna_solar = int(input("""Please Select from the options below:
        Select 1 to view Moon rise and set:
        Select 2 to view Sun rise and set:
        Select 3 to view Sun and Moon details together:
         """))
        while luna_solar != 1 and luna_solar != 2 and luna_solar != 3:
            luna_solar = int(input("""Please Select from the options below:
        Select 1 to view Moon rise and set:
        Select 2 to view Sun rise and set:
        Select 3 to view Sun and Moon details together:
         """))

        if luna_solar == 1:
            return self.moon_combined
        elif luna_solar == 2:
            return self.sun_combined
        elif luna_solar == 3:
            return self.moon_combined + "\n" + self.sun_combined


moons = ApiMoon()

print(moons.object_for_date())
