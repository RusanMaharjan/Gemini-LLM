import os
from google import genai

client = genai.Client(api_key=os.getenv("GEMINI_API_KEy"))


def prompt_llm(prompt):
    response = client.models.generate_content(
        model = "gemini-2.5-flash",
        contents = prompt
    )
    return response.text
