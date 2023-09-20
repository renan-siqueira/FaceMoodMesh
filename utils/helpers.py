import json


def load_json(filepath):
    """
    Loads a JSON file and returns its content.

    Parameters:
    - filepath (str): The path to the JSON file to be read.

    Returns:
    - dict: The content of the JSON file as a dictionary.
    """
    
    with open(filepath, 'r', encoding='utf-8') as file:
        messages = json.load(file)
    return messages
