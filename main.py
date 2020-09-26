from datetime import datetime
from location import ApiLocation
from planets import ApiMoon


now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)


greeting = "Welcome to ASTROAPP V1.0"
print(greeting)

here = ApiLocation()

print(here.city())


moons = ApiMoon()

print(moons.object_for_date())
