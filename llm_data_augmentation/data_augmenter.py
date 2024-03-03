import logging
from llm_data_augmentation.API.pesticide_management.answering_using_APIs import answer_question_about_pesticide
from llm_data_augmentation.API.weather_management.answering_using_APIs import answer_question_about_weather
from llm_data_augmentation.RAG.medicines_management.retriever_for_medecine import DocumentSearcher
from choose_data_augmentation.choose_data_augmentation import choose_data_augmentation

class DataAugmenter:
    """
    This class is responsible for building the context string for the model by fetching external data relevant to the input question.
    """
    def __init__(self, api_key: str, model: str = "mistral-medium"):
        self.api_key = api_key
        self.model = model
        self.search_db = DocumentSearcher()

    def augment_context(self, question: str) -> str:
        """Fetches external data based on the question and returns a context string."""
        context_parts = []
        api_needed = choose_data_augmentation(question, self.api_key, self.model)

        try:
            if 'current_weather' in api_needed:
                weather_info = answer_question_about_weather(question, self.api_key, self.model)
                context_parts.append(f"Infos météo : {weather_info}")

            if 'animal_medecines' in api_needed:
                medicine_info = self.search_db(question)
                context_parts.append(f"Infos médicament : {medicine_info}")

            if 'pesticides' in api_needed:
                pesticide_info = answer_question_about_pesticide(question, self.api_key, self.model)
                context_parts.append(f"Infos pesticide : {pesticide_info}")
        except Exception as e:
            logging.error(f"Error augmenting context: {e}")
            context_parts.append("Erreur lors de l'obtention des informations externes.")

        return " ".join(context_parts)
