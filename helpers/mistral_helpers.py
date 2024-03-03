from mistralai.client import MistralClient

def initialize_client(api_key: str) -> MistralClient:
    """
    Initialize the Mistral AI client with the provided API key.
    
    Parameters:
        api_key (str): The API key for authenticating with the Mistral AI service.
    
    Returns:
        MistralClient: An instance of the MistralClient.
    """
    if not api_key:
        raise ValueError("API key is required.")
    return MistralClient(api_key=api_key)