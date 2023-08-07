"""
This module provides functions for determining characteristics of a source.
"""

import datetime
import logging
import secrets
import string
import uuid
from babel import default_locale, UnknownLocaleError
from babel.dates import format_datetime
from intel.definitions import SOURCE_SCHEMA_VERSION, PATH_TO_SOURCE_MODEL, SOURCE_EXTENSION_YAML
from intel.source.my_yaml import read

py_logger5 = logging.getLogger(__name__)
py_logger5.setLevel(logging.INFO)

py_handler = logging.FileHandler(f"logs/{__name__}.log", mode='w')
py_formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")

py_handler.setFormatter(py_formatter)
py_logger5.addHandler(py_handler)


def extract_items_from_list(new_values, model):
    """
    Process the new_values dictionary and handle fields with type "list string separator comma".

    :param new_values: A dictionary containing field names and their values.
    :param model: The dictionary representing the model containing field properties and options.
    :return: None
    """
    py_logger5.info("extract_items_from_list function was called")

    for field, value in new_values.items():
        field_type = model.get(field, {}).get('type', '')
        if 'list string separator comma' in field_type:
            py_logger5.info(f"type 'list string separator comma' in {field_type}")
            extracted_items = [item.strip() for item in value.split(',') if item.strip()]
            new_values[field] = extracted_items
            py_logger5.info("items were extract")

    return new_values


def generate_id():
    """
    Generate unique string based on uuid4.

    :return: identifier for source.
    :rtype: str.
    """
    py_logger5.info("generate_id function was called")
    return str(uuid.uuid4())


def set_type():
    """
    Define the type of source. 1 - for human.

    :return: code for type of source.
    :rtype: int.
    """
    py_logger5.info("set_type function was called")
    return 1


def generate_invite(model):
    """
    Generate a list of unique invites.

    :return: list of invites, each of invite being a string.
    :rtype: list.
    """
    py_logger5.info("generate_invite function was called")

    alphabet: str = string.ascii_uppercase + string.digits
    py_logger5.info("Alphabet was written from the string module")
    invite = []

    charset_blacklist = model.get('invite', {}).get('charset', {}).get('blacklist', ['B8CDO0QIJ1GS5'])
    py_logger5.info("Blacklist was written from the model")

    invite_length = model.get('invite', {}).get('length', {}).get('min', 2)
    py_logger5.info("List length was written from the model")

    invite_item_length = model.get('invite', {}).get('item', {}).get('length', 7)
    py_logger5.info("Length of invite was written from the model")

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
    py_logger5.info("get_time function was called")

    return int(datetime.datetime.now().timestamp())


def create_stub():
    """
    Create an empty source dictionary with default values.

    :return: The created source dictionary.
    :rtype: Dict[str, Any]
    """
    py_logger5.info("create_stub function was called")

    time_of_creation = get_time()
    py_logger5.info("Time of creation was set")

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
    py_logger5.info("get_system_locale function was called")

    user_locale: str = default_locale()

    return user_locale or 'en_US'


def convert_date(value, user_locale):
    """
    Helper function to format date values in the desired format.

    :param: The value to be formatted.

    :return: The formatted value as a string.
    :rtype: str.
    """
    py_logger5.info("convert_date function was called")

    if isinstance(value, int):
        try:
            d_t = datetime.datetime.fromtimestamp(value)
            formatted_date = format_datetime(d_t, format='short', locale=user_locale)
            py_logger5.info(f"Date {value} formatted using locale {user_locale}")
            return formatted_date
        except UnknownLocaleError as error:
            py_logger5.error(f"Error formatting date: {error}")
            print(f"Error formatting date: {error}")

    return str(value)


def print_dictionary(dictionary, model):
    """
    Print the information contained in the dictionary.

    :param: dictionary (Dict[str, Any]): The dictionary.
    """
    py_logger5.info("print_dictionary function was called")

    sorted_items = sorted(dictionary.items())
    for key, value in sorted_items:
        if key in model and model[key].get('type') == 'date':
            py_logger5.info(f"Converting date value for key '{key}' to human-readable format.")
            value = convert_date(value, get_system_locale())
        if not value:
            py_logger5.warning(f"The value for key '{key}' is empty.")
            value = 'the field is empty'

        print(f'{key}: {value}')


def replace_hyphen_with_underscore(input_string):
    """
    Replace hyphens with underscores in the input string.

    :param input_string: The input string where hyphens need to be replaced.
    :return: The modified string with hyphens replaced by underscores.
    """
    py_logger5.info("replace_hyphen_with_underscore function was called")

    return input_string.replace('-', '_')
