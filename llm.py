import openai
from info import api_key

class OpenAILanguageModel:
    def __init__(self, api_key):
        openai.api_key = api_key

    def generate(self, query):
        prompt = f"Q: {query}\nA:"
        try:
            response = openai.Completion.create(
              engine="gpt-3.5-turbo",  # Change the engine as per your requirements
              prompt=prompt,
              max_tokens=1024,
              n=1,
              stop=None,
              temperature=0.5,
            )
            return response.choices[0].text.strip()
        except Exception as e:
            print(f"Failed to generate response: {e}")
            return None
