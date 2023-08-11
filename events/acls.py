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
    # picture_url = {
    #     "picture_url": api_dict["photos"][0]["src"]["original"]
    # }
    # return picture_url


def get_weather_data(city, state):
    geo_params = {
        "q": f"{city}, {state},",
        "appid": OPEN_WEATHER_API_KEY
    }
    # Create the URL for the geocoding API with the city and state
    geo_url = "http://api.openweathermap.org/geo/1.0/direct"
    # Make the request
    response = requests.get(geo_url, geo_params=geo_params)
    # Parse the JSON response
    geo_content = response.json()
    if not geo_content:
        return None

    # Get the latitude and longitude from the response
    latitude = geo_content[0]["lat"]
    longitude = geo_content[0]["lon"]
    # Create the URL for the current weather API with the latitude
    # and longitude
    weather_params = {
        "lat": latitude,
        "lon": longitude,
        "appid": OPEN_WEATHER_API_KEY,
        "units": "imperial",
    }
    weather_url = "https://api.openweathermap.org/data/2.5/weather"
    # Make the request
    response = requests.get(weather_url, weather_params=weather_params)
    # Parse the JSON response
    weather_content = response.json()
    if "main" not in weather_content or "weather" not in weather_content:
        return None
    # Get the main temperature and the weather's description and put
    # them in a dictionary
    temp = weather_content["main"]["temp"]
    weather_description = weather_content["weather"][0]["description"]
    # Return the dictionary
    weather = {
        "temp": temp,
        "description": weather_description
    }
    return weather
