import json
import re


def save_json(file_path, data):
    """
    Saves the given data as JSON in the specified file path.

    Args:
        file_path (str): The path to save the JSON file.
        data: The data to be saved as JSON.
    """
    with open(file_path, 'w') as f:
        json.dump(data, f)


def remove_whitespace(text):
    """
    Removes any weird whitespaces from the given text.

    Args:
        text (str): The text to remove whitespace from.

    Returns:
        str: The text with whitespace removed.
    """
    return ' '.join(text.split())


def clean_text(text):
    """
    Cleans the text by removing unnecessary characters and extra whitespaces.

    Args:
        text (str): The text to be cleaned.

    Returns:
        str: The cleaned text.
    """
    cleaned_text = re.sub(r'\s+', ' ', text)  # Replace multiple whitespaces with a single space
    cleaned_text = re.sub(r'\n+', ' ', cleaned_text)  # Replace newlines with a space
    cleaned_text = cleaned_text.strip()  # Remove leading and trailing whitespaces

    return cleaned_text
