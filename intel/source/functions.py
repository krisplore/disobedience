"""
This module provides functions for determining characteristics of a source.
"""

import datetime
import secrets
import string
import uuid

from babel import UnknownLocaleError, default_locale
from babel.dates import format_datetime

from intel.definitions import (PATH_TO_MODEL_SOURCE, SOURCE_EXTENSION_YAML,
                               SOURCE_SCHEMA_VERSION)
from intel.logger import logger
from intel.source.yaml import load
from intel.types.process import write


def generate_id():
    """
    Generate unique string based on uuid4.

    :return: identifier for source.
    :rtype: str.
    """
    generated_id = str(uuid.uuid4())
    if generated_id:
        logger.debug("Id was generated")
    return generated_id


def set_type():
    """
    Define the type of source. 1 - for human.

    :return: code for type of source.
    :rtype: int.
    """

    return 1


def generate_invite(model):
    """
    Generate a list of unique invites.

    :return: list of invites, each of invite being a string.
    :rtype: list.
    """

    alphabet: str = string.ascii_uppercase + string.digits
    if alphabet:
        logger.debug("Alphabet was written from the string module")
    invite = []

    charset_blacklist = model.get('invite', {}).get('charset', {}).get('blacklist', ['B8CDO0QIJ1GS5'])
    if charset_blacklist:
        logger.debug("Blacklist was written from the model")

    invite_length = model.get('invite', {}).get('length', {}).get('min', 2)
    if invite_length:
        logger.debug("List length was written from the model")

    invite_item_max_length = model.get('invite', {}).get('item', {}).get('length', {}).get('max', 7)
    if invite_item_max_length:
        logger.debug("Length of invite was written from the model")

    characters: list[str] = [c for c in alphabet if c not in charset_blacklist]

    for _ in range(invite_length):
        token_bytes: bytes = secrets.token_bytes(invite_item_max_length)
        invite.append(''.join(characters[b % len(characters)] for b in token_bytes))
    if invite:
        logger.debug("Invite was generated")

    return invite


def get_time():
    """
    Record the time the data was sent.

    :return: time of creation source data.
    :rtype: int
    """
    time = int(datetime.datetime.now().timestamp())
    if time:
        logger.debug("time was received")

    return time


def create_stub():
    """
    Create an empty source dictionary with default values.

    :return: The created source dictionary.
    :rtype: Dict[str, Any]
    """

    time_of_creation = get_time()
    if time_of_creation:
        logger.debug("Time of creation was set")

    source = {
        '_schema_version': SOURCE_SCHEMA_VERSION,
        'callsign': '',
        'tags': '',
        'invited_by': '',
        'id': generate_id(),
        'type': set_type(),
        'reliability': '',
        'note': '',
        'created': time_of_creation,
        'modified': time_of_creation,
        'invite': generate_invite(load(PATH_TO_MODEL_SOURCE + SOURCE_EXTENSION_YAML)),
        'stats': {
            'facts': {
                'total': 0,
                'confirmed': 0,
                'refuted': 0
            }
        }
    }
    if source:
        logger.debug("The source stub was created")

    return source


def get_system_locale():
    """
    Get the system locale of the user.

    :return: system locale of the user as a string in the format 'language_region'.
    :rtype:str
    """

    user_locale: str = default_locale()
    if user_locale:
        logger.debug("system locale was found")
        return user_locale
    logger.info("en_US locale was set")
    return 'en_US'


def convert_date(value, user_locale):
    """
    Helper function to format date values in the desired format.

    :param: The value to be formatted.

    :return: The formatted value as a string.
    :rtype: str.
    """

    if isinstance(value, int):
        try:
            d_t = datetime.datetime.fromtimestamp(value)
            formatted_date = format_datetime(d_t, format='short', locale=user_locale)
            logger.debug("Date %s formatted", value)
            return formatted_date
        except UnknownLocaleError as error:
            logger.error("Error formatting date: %s", error)
            print("Error formatting date: %s", error)

    return str(value)


def print_dictionary(dictionary, model):
    """
    Print the information contained in the dictionary.

    :param: dictionary (Dict[str, Any]): The dictionary.
    """

    dictionary = write(dictionary, model)
    sorted_items = sorted(dictionary.items())
    for key, value in sorted_items:
        if key in model and model[key].get('type') == 'date':
            value = convert_date(value, get_system_locale())
        if not value:
            logger.debug("The value for key '%s' is empty.", key)
            value = 'the field is empty'

        print(f'{key}: {value}')
        logger.debug("The result was printed")


def sync_name(input_string):
    """
    Replace hyphens with underscores in the input string.

    :param input_string: The input string where hyphens need to be replaced.
    :return: The modified string with hyphens replaced by underscores.
    """
    output_string = input_string.replace('-', '_')
    if output_string:
        logger.debug("The %s has been synchronized with the model", input_string)

    return output_string
