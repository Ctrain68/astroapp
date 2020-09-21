from datetime import datetime 
from datetime import date
import socket
import json
import urllib.request
import requests

# hostname = socket.gethostname()
# local_ip = socket.gethostbyname(hostname)

# print(local_ip)

external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')

print(external_ip)

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)



class ApiLocation:
    



    def __init__(self):
        self.url = "http://api.ipstack.com/"
        self.ip = self.get_ip()
        self.connector = "?access_key="
        self.key = "60a96c2830ff498d19b2ff0f2de5fd6a"
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


 
# print(here.location())

# date_selected = "2020-06-05"

class ApiMoon:
    


    def __init__(self):
        self.url = "https://api.ipgeolocation.io/astronomy?apiKey="
        self.key = "a22d39a1a1c14c2b863b0f340ca8ab80"
        self.connector = "&location="
        self.location = here.city()
        self.date_connector = "&date="
        self.date_selected = self.get_date()
        self.any_date = self.for_date()
        self.sunrise = "Sunrise time is "
        self.sunset = " Sunset time is "
        self.moonrise = "Moonrise time is "
        self.moonset = " Mooonset time is "



    def get_date(self):
        enter_date = int(input("Please select 1 to use current date or 2 to enter in a date of your choice: "))
        while enter_date != 1 and enter_date != 2:

            enter_date = int(input("Please select 1 to use current date or 2 to enter in a date of your choice: "))

        if enter_date == 1:
            today = date.today()
            
            todays_date= today.strftime("%Y-%m-%d")
            print(f"You have selected {todays_date} as your date")
            return todays_date

        elif enter_date == 2:
            year = input("Enter year ")
            month = input("Enter Month MM")
            day = input("Enter Date DD")
            other_date = f"{year}-{month}-{day}"
            print(f"You have selected {other_date} as your date")
            return other_date

    def get(self):
        return requests.get(self.url+self.key+self.connector+self.location+self.date_connector+self.date_selected)


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
            return self.moonrise+str(self.any_date['moonrise'])+self.moonset+str(self.any_date["moonset"])
        elif luna_solar == 2:
            return self.sunrise+str(self.any_date['sunrise'])+self.sunset+str(self.any_date["sunset"])
        elif luna_solar == 3:
            return self.moonrise+str(self.any_date['moonrise'])+self.moonset+str(self.any_date["moonset"]) + "\n" + self.sunrise+str(self.any_date['sunrise'])+self.sunset+str(self.any_date["sunset"])
    
        

        



moons = ApiMoon()


 
print(moons.object_for_date())

