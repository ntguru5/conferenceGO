import requests
from .keys import PEXELS_API_KEY, OPEN_WEATHER_API_KEY


def get_picture_url(query):
    """
    Get photos of a city using the Pexels API
    """
    url = f"https://api.pexels.com/v1/search?query={query}"

    headers = {
        "Authorization": PEXELS_API_KEY,
    }

    response = requests.get(url, headers=headers)
    api_dict = response.json()
    return api_dict["photos"][0]["src"]["original"]


def get_weather_data(city, state):
    params = {
        "q": f"{city}, {state}",
        "appid": OPEN_WEATHER_API_KEY,
    }
    # Create the URL for the geocoding API with the city and state
    url = "http://api.openweathermap.org/geo/1.0/direct"
    # Make the request
    response = requests.get(url, params=params)
    # Parse the JSON response
    content = response.json()
    if not content:
        return None

    # Get the latitude and longitude from the response
    latitude = content[0]["lat"]
    longitude = content[0]["lon"]
    # Create the URL for the current weather API with the latitude
    # and longitude
    params = {
        "lat": latitude,
        "lon": longitude,
        "appid": OPEN_WEATHER_API_KEY,
        "units": "imperial",
    }
    url = "https://api.openweathermap.org/data/2.5/weather"
    # Make the request
    response = requests.get(url, params=params)
    # Parse the JSON response
    content = response.json()
    if "main" not in content or "weather" not in content:
        return None
    # Get the main temperature and the weather's description and put
    # them in a dictionary
    temperature = content["main"]["temp"]
    weather_description = content["weather"][0]["description"]
    # Return the dictionary
    weather_dict = {
        "temp": temperature,
        "description": weather_description
    }
    return weather_dict
