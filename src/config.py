import os
import sys
import json

from termcolor import colored

ROOT_DIR = os.path.dirname(sys.path[0])

def assert_folder_structure() -> None:
    """
    Make sure that the nessecary folder structure is present.

    Returns:
        None
    """
    # Create the .mp folder
    if not os.path.exists(os.path.join(ROOT_DIR, '.mp')):
        if get_verbose():
            print(colored(f"=> Creating .mp folder at {os.path.join(ROOT_DIR, '.mp')}", 'green'))
        os.makedirs(os.path.join(ROOT_DIR, '.mp'))

def get_first_time_running() -> bool:
    """
    Checks if the program is running for the first time by checking if .mp folder exists.

    Returns:
        exists (bool): True if the program is running for the first time, False otherwise
    """
    return not os.path.exists(os.path.join(ROOT_DIR, '.mp'))

def get_email_credentials() -> dict:
    """
    Gets the email credentials from the config file.

    Returns:
        credentials (dict): The email credentials
    """
    with open(os.path.join(ROOT_DIR, 'config.json'), 'r') as file:
        return json.load(file)['email']

def get_verbose() -> bool:
    """
    Gets the verbose flag from the config file.

    Returns:
        verbose (bool): The verbose flag
    """
    with open(os.path.join(ROOT_DIR, 'config.json'), 'r') as file:
        return json.load(file)['verbose']

def get_firefox_profile_path() -> str:
    """
    Gets the path to the Firefox profile.

    Returns:
        path (str): The path to the Firefox profile
    """
    with open(os.path.join(ROOT_DIR, 'config.json'), 'r') as file:
        return json.load(file)['firefox_profile']

def get_headless() -> bool:
    """
    Gets the headless flag from the config file.

    Returns:
        headless (bool): The headless flag
    """
    with open(os.path.join(ROOT_DIR, 'config.json'), 'r') as file:
        return json.load(file)['headless']

def get_model() -> str:
    """
    Gets the model from the config file.

    Returns:
        model (str): The model
    """
    with open(os.path.join(ROOT_DIR, 'config.json'), 'r') as file:
        return json.load(file)['llm_model']

def get_twitter_language() -> str:
    """
    Gets the Twitter language from the config file.

    Returns:
        language (str): The Twitter language
    """
    with open(os.path.join(ROOT_DIR, 'config.json'), 'r') as file:
        return json.load(file)['twitter_language']
