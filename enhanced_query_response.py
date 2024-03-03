import os
import logging
from dotenv import load_dotenv

from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
from llm_data_augmentation.data_augmenter import DataAugmenter
from helpers.construct_prompt import construct_prompt

logging.basicConfig(level=logging.INFO)
load_dotenv()

API_KEY = os.getenv('API_KEY')
MODEL = os.getenv('MODEL')
if not API_KEY:
    logging.error("API_KEY not found in environment variables.")
    exit(1)

def call_llm(question: str, api_key: str, model: str = "mistral-medium") -> str:
    """Calls the LLM with the constructed prompt and returns the LLM's response.
    Handles errors gracefully and logs key actions for troubleshooting."""
    try:
        data_augmenter = DataAugmenter(api_key, model)
        additional_context = data_augmenter.augment_context(question)
        prompt = construct_prompt(question, additional_context)

        client = MistralClient(api_key=api_key)
        messages = [ChatMessage(role="user", content=prompt)]

        chat_response = client.chat(model=model, messages=messages)
        return chat_response.choices[0].message.content
    except Exception as e:
        logging.error(f"Error calling LLM: {e}")
        return "An error occurred while processing the request."

if __name__ == "__main__":
    question = "Quel est le médicament pour traiter la coccidiose chez les poules ?"
    try:
        response = call_llm(question, API_KEY)
        print(f'Response to "{question}": {response}')
    except Exception as e:
        logging.error(f"Failed to get response: {e}")
