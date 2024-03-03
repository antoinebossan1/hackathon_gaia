import requests
import logging
from .extract_substance_name_from_prompt import extract_substance_name_from_prompt

def check_pesticide_approval(question: str, api_key: str, model: str = "mistral-medium") -> str:
    pesticide_name = extract_substance_name_from_prompt(question, api_key, model)

    """
    Checks if the specified pesticide is approved using the EU Pesticides Database API.

    Parameters:
        pesticide_name (str): The name of the pesticide to check.

    Returns:
        str: Approval status of the pesticide.
    """
    API_URL = "https://api.datalake.sante.service.ec.europa.eu/sante/pesticides/active_substances"
    params = {
        'skip': 0,
        'take': 100,
        'substance_name': pesticide_name,
        'api-version': 'v1.0'
    }
    headers = {'Cache-Control': 'no-cache'}

    try:
        response = requests.get(API_URL, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()

        if not data:
            return "No data found for the specified pesticide."

        first_result = data[0]
        substance_status = first_result.get('substance_status', 'Unknown')
        return f"Pesticide '{pesticide_name}' status: {substance_status}"

    except requests.RequestException as e:
        logging.error(f"Error fetching pesticide approval status: {e}")
        return f"Error fetching pesticide approval status: {e}"

