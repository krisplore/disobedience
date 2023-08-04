"""
This module provides functions for determining characteristics of a source.
"""

import datetime
import secrets
import string
import uuid
from babel import default_locale, UnknownLocaleError
from babel.dates import format_datetime
from intel.definitions import SOURCE_SCHEMA_VERSION, PATH_TO_SOURCE_MODEL, SOURCE_EXTENSION_YAML
from intel.source.my_yaml import read


def extract_items_from_list(new_values, model):
    """
    Process the new_values dictionary and handle fields with type "list string separator comma".

    :param new_values: A dictionary containing field names and their values.
    :param model: The dictionary representing the model containing field properties and options.
    :return: None
    """
    for field, value in new_values.items():
        field_type = model.get(field, {}).get('type', '')
        if 'list string separator comma' in field_type:
            extracted_items = [item.strip() for item in value.split(',') if item.strip()]
            new_values[field] = extracted_items


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
    alphabet: str = string.ascii_uppercase + string.digits
    invite = []
    charset_blacklist = model.get('invite', {}).get('charset', {}).get('blacklist', ['B8CDO0QIJ1GS5'])
    invite_item_length = model.get('invite', {}).get('item', {}).get('length', 7)
    invite_length = model.get('invite', {}).get('length', 2)

    characters: list[str] = [c for c in alphabet if c not in charset_blacklist]

    for _ in range(invite_length):
        token_bytes: bytes = secrets.token_bytes(invite_item_length)
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
        'invited_by': '',
        'id': generate_id(),
        'type': set_type(),
        'reliability': 4.98,
        'note': '',
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


def print_dictionary(dictionary, model):
    """
    Print the information contained in the dictionary.

    :param: dictionary (Dict[str, Any]): The dictionary.
    """

    sorted_items = sorted(dictionary.items())
    for key, value in sorted_items:
        if key in model and model[key].get('type') == 'date':
            value = convert_date(value, get_system_locale())
        if not value:
            value = 'the field is empty'
        print(f'{key}: {value}')


def replace_hyphen_with_underscore(input_string):
    """
    Replace hyphens with underscores in the input string.

    :param input_string: The input string where hyphens need to be replaced.
    :return: The modified string with hyphens replaced by underscores.
    """
    return input_string.replace('-', '_')
