import requests
from typing import Tuple

def fetch_coordinates(city_name: str) -> Tuple[float, float]:
    """
    Fetches the latitude and longitude for a given city name using the Open Street Map API.

    Parameters:
    - city_name (str): The name of the city.

    Returns:
    - Tuple[float, float] or None: A tuple containing the latitude and longitude of the city if successful; otherwise, None.
    """
    osm_url = f"https://nominatim.openstreetmap.org/search?city={city_name}&format=json"
    try:
        response = requests.get(osm_url)
        response.raise_for_status()
        data = response.json()
        if data:
            return float(data[0]['lat']), float(data[0]['lon'])
        else:
            return None
    except Exception as e:
        print(f"Error fetching coordinates for {city_name}: {e}")
        return None
