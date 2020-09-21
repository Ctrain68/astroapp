from datetime import datetime 
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


 
print(here.location())

date_selected = "2020-06-05"

class ApiMoon:
    


    def __init__(self):
        self.url = "https://api.ipgeolocation.io/astronomy?apiKey="
        self.key = "a22d39a1a1c14c2b863b0f340ca8ab80"
        self.connector = "&location="
        self.location = here.city()
        self.date_connector = "&date="
        self.date_selected = date_selected
        


    
    def get(self):
        return requests.get(self.url+self.key+self.connector+self.location)

    def get_date(self):
        print(self.url+self.key+self.connector+self.location+self.date_connector+self.date_selected)
        return requests.get(self.url+self.key+self.connector+self.location+self.date_connector+self.date_selected)

    # def date(self, date_entry):
    #     self.date_entry = date_entry
    def solarfordate(self):
        data = json.loads(self.get_date().text)
        # print(json.loads(data.text))
        return (f"Sunrise is {data['sunrise']} and sunset is {data['sunset']}")

    def lunarfordate(self):
        data = json.loads(self.get_date().text)
        # print(json.loads(data.text))
        return (f"Sunrise is {data['sunrise']} and sunset is {data['sunset']}")

    def moon(self):
        data = json.loads(self.get().text)
        # print(json.loads(data.text))
        return (f"Sunrise is {data['sunrise']} and sunset is {data['sunset']}")   

    def moon(self):
        data = json.loads(self.get().text)
        # print(json.loads(data.text))
        return (f"Moonrise is {data['moonrise']} and moonset is {data['moonset']}")   
        

# print(ApiLocation.stuff)

moons = ApiMoon()


 
print(moons.moon())
print(moons.solarfordate())

# class ApiSun:
    


#     def __init__(self):
#         self.url = "https://api.ipgeolocation.io/astronomy?apiKey="
#         self.key = "a22d39a1a1c14c2b863b0f340ca8ab80"
#         self.connector = "&location="
        
#         self.location = here.city()

    
#     def get(self):
#         return requests.get(self.url+self.key+self.connector+self.location)

#     def moon(self):
#         data = json.loads(self.get().text)
#         # print(json.loads(data.text))
#         return (f"Moonrise is {data['sunrise']} and moonset is {data['sunset']}")
        

# print(ApiLocation.stuff)

moons = ApiMoon()


 
print(moons.moon())
#     response = ""


#     def __init__(self):
#         pass
    
#     def response(self):
#         info = requests.get(f"http://api.ipstack.com/60.242.75.5?access_key=60a96c2830ff498d19b2ff0f2de5fd6a") 
#         return info
    
#     def word(self):
#         data = json.loads(self.response().text)
#         return (f"This is your city {data['city']}")



# print(ApiLocation.word())
        




   
    
    
# class File_handler:
#      def write_word_to_file(....):
         
# class Word:
#     def ...
    
    
# main:
#     user input?
    
# if:
#     get_word_from_api
#     write word to file:
# # else:
#     find_wird_in_fi