from datetime import datetime
from location import ApiLocation
from planets import ApiMoon

'''Functions to return current
time when the application is run'''
now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("The Time is ", current_time)


greeting = "Welcome to ASTROAPP V1.0"
print(greeting)
''' Calls the class API Location to return
city location based on public IP Address'''
location = ApiLocation()

print(
    "Your location has automatically been selected based on IP as " +
    location.city())

''' Calls the API Moon class to return Sunrise/set
 and Moonrise/set based on date selected'''

moons = ApiMoon()

print(moons.object_for_date())
