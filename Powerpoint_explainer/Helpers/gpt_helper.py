import openai
import os


def generate_explanation(prompt, slide_number):
    """
    Sends a request to the GPT-3.5 API and returns the AI's reply.

    Args:
        prompt (str): The prompt for the AI model.

    Returns:
        str: The AI's generated explanation.
    """
    full_prompt = f"Explain the content of slide {slide_number}:\n{prompt}"
    key_path = os.path.join(os.path.dirname(__file__), 'openai_key.txt')
    if not os.path.exists(key_path):
        raise FileNotFoundError("OpenAI API key file not found.")
    with open(key_path, 'r') as f:
        api_key = f.read().strip()

    openai.api_key = api_key

    try:
        response = openai.Completion.create(
            engine='text-davinci-003',  # Use GPT-3.5 Turbo engine
            prompt=prompt,
            max_tokens=300,  # Adjust as per your requirements
            n=1,  # Number of responses to generate
            stop=None,  # Stop condition for the generated response
            timeout=10,  # Timeout in seconds (adjust as per your needs)
        )
        return response.choices[0].text.strip()
    except openai.OpenAIAPIError as e:
        # Handle API errors
        raise Exception("OpenAI API Error: " + str(e))
    except Exception as e:
        # Handle other exceptions
        raise Exception("An error occurred during AI response generation: " + str(e))
