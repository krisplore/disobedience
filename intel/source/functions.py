"""
This module provides functions for determining characteristics of a source.
"""

import datetime
import secrets
import string
import uuid
from typing import Any
from babel import default_locale, UnknownLocaleError
from babel.dates import format_datetime
from intel.definitions import SOURCE_SCHEMA_VERSION, PATH_TO_SOURCE_MODEL, SOURCE_EXTENSION_YAML
from intel.source.yaml import read

# AMOUNT_OF_INVITE: int = 2
# CHARACTERS_FOR_EXCLUDE: str = 'B8CDO0QIJ1GS5'
# INVITE_LENGTH: int = 7
DATE_KEYS = ['created', 'modified']


def extract_tags(raw_tags):
    """
    Split a string by comma, remove spaces in the beginning and at the end of string.

    Arg:
       raw_tags (str): contain users tags separated by commas.

    :return: each of tags as separated element of list.
    :rtype: list.
    """

    tags: list[Any] = [item.strip() for item in raw_tags.split(',') if item.strip()]
    return tags


def generate_id():
    """
    Generate unique string based on uuid4.

    :return: identifier for source.
    :rtype: str.
    """

    return str(uuid.uuid4())


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
    amount_of_invite = model['invite']['length']
    characters_for_exclude = model['invite']['ignored charset']
    alphabet: str = string.ascii_uppercase + string.digits
    invite_length = model['invite']['item']['length']
    invite = []

    characters: list[str] = [c for c in alphabet if c not in characters_for_exclude]

    for _ in range(amount_of_invite):
        token_bytes: bytes = secrets.token_bytes(invite_length)
        invite.append(''.join(characters[b % len(characters)] for b in token_bytes))
    return invite


def get_time():
    """
    Record the time the data was sent.

    :return: time of creation source data.
    :rtype: int
    """

    return int(datetime.datetime.now().timestamp())


def create_stub():
    """
    Create an empty source dictionary with default values.

    :return: The created source dictionary.
    :rtype: Dict[str, Any]
    """

    time_of_creation = get_time()

    source = {
        '_source_schema_version': SOURCE_SCHEMA_VERSION,
        'callsign': '',
        'tags': '',
        'invited by': '',
        'id': generate_id(),
        'type': set_type(),
        'reliability': 4.98,
        'note': 'some new note',
        'created': time_of_creation,
        'modified': time_of_creation,
        'invite': generate_invite(read(PATH_TO_SOURCE_MODEL + SOURCE_EXTENSION_YAML)),
        'stats': {
            'facts': {
                'total': 0,
                'confirmed': 0,
                'refuted': 0
            }
        }
    }

    return source


def get_system_locale():
    """
    Get the system locale of the user.

    :return: system locale of the user as a string in the format 'language_region'.
    :rtype:str
    """
    user_locale: str = default_locale()

    return user_locale or 'en_US'


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
            return formatted_date
        except UnknownLocaleError as error:
            print(f"Error formatting date: {error}")

    return str(value)


def print_dictionary(dictionary):
    """
    Print the information contained in the dictionary.

    :param: dictionary (Dict[str, Any]): The dictionary.
    """

    sorted_items = sorted(dictionary.items())

    for key, value in sorted_items:
        if key in DATE_KEYS:
            value = convert_date(value, get_system_locale())
        if key == 'tags' and not value:
            value = 'the field is empty'
        print(f'{key}: {value}')
