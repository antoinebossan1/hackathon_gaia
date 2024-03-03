def construct_prompt(question: str, additional_context: str) -> str:
    """Constructs a prompt with or without additional context."""
    if additional_context:
        return f"With additional info: '{additional_context}', and the original question: '{question}', please provide an appropriate response in French."
    return f"Given the question: '{question}', please provide an appropriate response in French."