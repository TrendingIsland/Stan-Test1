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

    def ask(self):
        """
        Generates text based on the provided message using the OpenAI API.

        Returns
            str: The generated text containing answers to user queries.
        """
        # Create a completion request
        history = "" 
        while(True):
            message = input("\nEnter STOP to stop the program \n continous running will cause credit to decrease \nEnter Your Query: \n ")
            if message != "STOP":
                history =  history+"\n new query: "+message
                completion = self.client.chat.completions.create(
                    model="gpt-3.5-turbo",  # Specify the GPT model
                    messages=[
                        {"role": "system", "content": history},
                    ]
                )
                # Return the generated text
                history += "\n Answer: "+completion.choices[0].message.content + "\n"
            else:
                break
            
        return history

# Retrieve the API key from environment variables
api_key = os.getenv("CG_KEY")

# Create an instance of the Generate class
generator = GP_Generate(api_key)

# Generate text based on the provided message

result = generator.ask()
print(result)