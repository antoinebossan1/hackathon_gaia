from dotenv import load_dotenv
import os
import logging
from mistralai.client import MistralClient
from .helpers.extract_city_name import extract_city_name
from .helpers.fetch_coordinates import fetch_coordinates
from .helpers.fetch_weather_in_french import fetch_weather_in_french

logging.basicConfig(level=logging.INFO)

load_dotenv()

API_KEY = os.getenv('API_KEY')
MODEL = os.getenv('MODEL')
client = MistralClient(api_key=API_KEY)

def setup_mistral_client(api_key: str) -> MistralClient:
    """Setup the Mistral AI client."""
    return MistralClient(api_key=api_key)

def answer_question_about_weather(user_question: str, api_key: str, model: str) -> str:
    """
    Answers user's weather-related question in French.
    
    Args:
        user_question (str): The user's question about the weather.
        api_key (str): API key for external service.
        model (str): Model name for the external service.
    
    Returns:
        str: The answer to the user's question in French.
    """
    try:
        # Extract city name
        city_name = extract_city_name(user_question, api_key, model)
        logging.info(f'City name: {city_name}')
        # Fetch coordinates
        lat, lon = fetch_coordinates(city_name)
        # Prepare weather message in French
        weather_message = fetch_weather_in_french(lat, lon)
        return weather_message
    except Exception as e:
        logging.error(f'Error answering question about weather: {e}')
        return "Désolé, je ne peux pas répondre à votre question en ce moment."

if __name__ == "__main__":
    user_question = "Quelle est la météo à Paris aujourd'hui ?"
    answer = answer_question_about_weather(user_question, API_KEY, MODEL)
    logging.info(f'Answer to "{user_question}": {answer}')
