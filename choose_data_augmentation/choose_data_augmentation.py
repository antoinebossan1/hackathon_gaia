from dotenv import load_dotenv
import os

from mistralai.models.chat_completion import ChatMessage
from helpers.mistral_helpers import initialize_client

load_dotenv()
api_key = os.getenv('API_KEY')

def choose_data_augmentation(question: str, api_key: str, model: str = "mistral-medium") -> str:
    """
    Determine if data augmentation is needed based on the question, using the Mistral AI service.
    
    Parameters:
        question (str): The question to evaluate for data augmentation.
        api_key (str): The API key for authenticating with the Mistral AI service.
        model (str, optional): The model to use for the chat completion. Defaults to "mistral-medium".
    
    Returns:
        str: The name of the databases needed for the question, if any.
    """
    prompt = f"Given the question: '{question}' if you judge it would be useful to include data from one the following database: [current_weather, animal_medecines, pesticides], just return the name of each database under a list format, do not return anything else in any case "
    client = initialize_client(api_key)
    messages = [ChatMessage(role="user", content=prompt)]
    
    try:
        chat_response = client.chat(model=model, messages=messages)
        return chat_response.choices[0].message.content
    except Exception as e:
        print(f"An error occurred: {e}")
        return ""
