from openai import OpenAI
import os

class GP_Generate:
    """
    A class for generating text using the OpenAI API.

    Attributes:
        api_key (str): The API key used to authenticate with the OpenAI API.
        client (OpenAI): An instance of the OpenAI class for making API requests.
    """

    def __init__(self, api_key):
        """
        Initializes the Generate class with the provided API key.

        Args:
            api_key (str): The API key used to authenticate with the OpenAI API.
        """
        self.client = OpenAI(api_key=api_key)

    def ask(self, message):
        """
        Generates text based on the provided message using the OpenAI API.

        Args:
            message (str): The input message for text generation.

        Returns:
            str: The generated text.
        """
        # Create a completion request
        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",  # Specify the GPT model
            messages=[
                {"role": "system", "content": message},
            ]
        )
        # Return the generated text
        return completion.choices[0].message.content

# Retrieve the API key from environment variables
# api_key = os.getenv("API_KEY")

# # Create an instance of the Generate class
# generator = GP_Generate(api_key)

# # Generate text based on the provided message
# result = generator.ask("sing about pizza")

# Print the generated text
# print(result)
