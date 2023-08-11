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




# def get_weather_data(city, state):
    # Use the Open Weather API
