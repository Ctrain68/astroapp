# AstroApp V0.1

This is an app that returns sunrise/set and moonrise/set for a specific date and location.

The location returned for this application is dependant on your public IP address. If you use a VPN or cloud service to run this applicaiton this will not be accurate. Future versions will have an option to select location manually as well as other astronomical objects.

## About the App

Astroapp provides an algorithmic solution to gaining both sun rise/set and moon rise/set for a specific location. Namely where the host IP is from and the sunrise/set moonrise/set for any date +/- 2000 years in that location.
It does this by first running an algorithm to determine the host computers public IP address. Which in turn is queried through a location API to determine the user location by IP address. Once this has been achieved details from the location API are returned in JSON format and converted to a dict for python use. 
This is the detail that shall be used in the app and is the city location. Once this has been achieved this is set as the default location. 
This is saved as a variable for a use in the second algorithm that shall return the sunrise/set and moonrise/se
Using this information the user is prompted to enter in the date they wish to know the sunrise/set, moonrise/set for. The have the option of using the current date which is returned in the correct format by a function or entering in their own date in the format required. This is sanitized to maintain accuracy of data. 
With the location and the date know known. This is passed into a class method to query an API to return the data for the selected day at that specific location.
The data is then converted from JSON into a dictionary for access in python.
Once the data has been returned the user is prompted for input to specify which data is required. Namely if they require Moonrise and Moonset, Sunrise and Sunset, or both data printed together. Once this selection is made the data is returned and the program ends.


## Flowchart

![Flowchart](/capture.jpg)


## Installation

### Dependancies

certifi==2020.6.20
chardet==3.0.4
DateTime==4.3
flake8==3.8.3
idna==2.10
mccabe==0.6.1
pycodestyle==2.6.0
pyflakes==2.2.0
python-dotenv==0.14.0
pytz==2020.1
requests==2.24.0
termcolor==1.1.0
urllib3==1.25.10
zope.interface==5.1.0


Clone the repository from this github.

Create a Python3.8 virtual environment and activiate

In your console run the following:

```bash
python3.8 -m venv venv
source venv/bin/activate
export LOCATION_API_KEY=60a96c2830ff498d19b2ff0f2de5fd6a
export MOON_API_KEY=a22d39a1a1c14c2b863b0f340ca8ab80

pip install -r requirements.txt

python3.8 main.py
```

## Usage Example
When you the application runs select from the menu to chose the date required.
You will then be prompted to choose to select current date or a date past or future +-2000years
You will then be prompted to choose which options you would like to be displayed.

These shall then be printed to the screen.






