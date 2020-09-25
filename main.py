
from location import ApiLocation
from location import ApiMoon


greeting = "Welcome to ASTROAPP V1.0"








here = ApiLocation()

print(here.city())


moons = ApiMoon()

print(moons.object_for_date())
