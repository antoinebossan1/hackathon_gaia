import os
import logging
from dotenv import load_dotenv
from mistralai.client import MistralClient
from .helpers.check_pesticide_approval import check_pesticide_approval

logging.basicConfig(level=logging.INFO)

load_dotenv()

API_KEY = os.getenv('API_KEY')
client = MistralClient(api_key=API_KEY)

def answer_question_about_pesticide(question: str, api_key: str, MODEL: str = "mistral-medium") -> str:
    """Determines the approval status of a pesticide."""
    approval_status = check_pesticide_approval(question, api_key, MODEL)
    return approval_status

if __name__ == "__main__":
    user_question = "Fenhexamid"
    answer = answer_question_about_pesticide(user_question)
    logging.info(f'Answer to "{user_question}": {answer}')
