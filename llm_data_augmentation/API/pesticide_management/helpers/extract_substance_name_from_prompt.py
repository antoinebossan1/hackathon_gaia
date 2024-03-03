from typing import Optional
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage

def extract_substance_name_from_prompt(question: str, api_key: str, model: str = "mistral-medium") -> Optional[str]:
    """
    Extracts the name of the active substance mentioned in a user's prompt using the specified LLM model.

    Parameters:
    - question (str): The user's prompt from which to extract the substance name.
    - api_key (str): API key for authenticating with the Mistral AI service.
    - model (str): The LLM model to use for the chat completion. Defaults to 'mistral-medium'.

    Returns:
    - Optional[str]: The name of the substance extracted from the user's prompt, or None if no substance could be identified.
    """
    prompt = f"From the following user prompt: '{question}', identify and extract the name of any active substance mentioned. Only return the substance name."

    client = MistralClient(api_key=api_key)
    messages = [ChatMessage(role="user", content=prompt)]

    try:
        chat_response = client.chat(model=model, messages=messages)
        substance_name = chat_response.choices[0].message.content.strip()
        return substance_name if substance_name else None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
