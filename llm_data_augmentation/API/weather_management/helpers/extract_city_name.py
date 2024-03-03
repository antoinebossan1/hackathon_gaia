from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage


def extract_city_name(question: str, api_key: str, model: str = "mistral-medium") -> str:
    """
    Extracts the name of a city mentioned in a question using the specified LLM model.

    Parameters:
    - question (str): The question from which to extract the city name.
    - api_key (str): API key for authenticating with the Mistral AI service.
    - model (str): The LLM model to use for the chat completion. Defaults to 'mistral-medium'.

    Returns:
    - Optional[str]: The name of the city extracted from the question, or None if no city could be identified.
    """
    prompt = f"Given the question: '{question}', identify and extract the name of the city mentioned. Just return the name of the city."

    client = MistralClient(api_key=api_key)
    messages = [ChatMessage(role="user", content=prompt)]

    try:
        chat_response = client.chat(model=model, messages=messages)
        city_name = chat_response.choices[0].message.content.strip()
        return city_name if city_name else None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
