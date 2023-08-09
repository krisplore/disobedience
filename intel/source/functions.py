"""
This module provides functions for determining characteristics of a source.
"""

import datetime
import secrets
import string
import uuid
from babel import default_locale, UnknownLocaleError
from babel.dates import format_datetime
from intel.definitions import SOURCE_SCHEMA_VERSION, PATH_TO_MODEL_SOURCE, SOURCE_EXTENSION_YAML
from intel.logger import setup as logger_setup
from intel.source.yaml import load
from intel.types.process import write

logger = logger_setup()


def generate_id():
    """
    Generate unique string based on uuid4.

    :return: identifier for source.
    :rtype: str.
    """
    logger.info("generate_id function was called")
    return str(uuid.uuid4())


def set_type():
    """
    Define the type of source. 1 - for human.

    :return: code for type of source.
    :rtype: int.
    """
    logger.info("set_type function was called")
    return 1


def generate_invite(model):
    """
    Generate a list of unique invites.

    :return: list of invites, each of invite being a string.
    :rtype: list.
    """
    logger.info("generate_invite function was called")

    alphabet: str = string.ascii_uppercase + string.digits
    logger.info("Alphabet was written from the string module")
    invite = []

    charset_blacklist = model.get('invite', {}).get('charset', {}).get('blacklist', ['B8CDO0QIJ1GS5'])
    logger.info("Blacklist was written from the model")

    invite_length = model.get('invite', {}).get('length', {}).get('min', 2)
    logger.info("List length was written from the model")

    invite_item_max_length = model.get('invite', {}).get('item', {}).get('length', {}).get('max', 7)
    logger.info("Length of invite was written from the model")

    characters: list[str] = [c for c in alphabet if c not in charset_blacklist]

    for _ in range(invite_length):
        token_bytes: bytes = secrets.token_bytes(invite_item_max_length)
        invite.append(''.join(characters[b % len(characters)] for b in token_bytes))
    return invite


def get_time():
    """
    Record the time the data was sent.

    :return: time of creation source data.
    :rtype: int
    """
    logger.info("get_time function was called")

    return int(datetime.datetime.now().timestamp())


def create_stub():
    """
    Create an empty source dictionary with default values.

    :return: The created source dictionary.
    :rtype: Dict[str, Any]
    """
    logger.info("create_stub function was called")

    time_of_creation = get_time()
    logger.info("Time of creation was set")

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

    return source


def get_system_locale():
    """
    Get the system locale of the user.

    :return: system locale of the user as a string in the format 'language_region'.
    :rtype:str
    """
    logger.info("get_system_locale function was called")

    user_locale: str = default_locale()

    return user_locale or 'en_US'


def convert_date(value, user_locale):
    """
    Helper function to format date values in the desired format.

    :param: The value to be formatted.

    :return: The formatted value as a string.
    :rtype: str.
    """
    logger.info("convert_date function was called")

    if isinstance(value, int):
        try:
            d_t = datetime.datetime.fromtimestamp(value)
            formatted_date = format_datetime(d_t, format='short', locale=user_locale)
            logger.info("Date %s formatted using locale %s", value, user_locale)
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
    logger.info("print_dictionary function was called")

    dictionary = write(dictionary, model)
    sorted_items = sorted(dictionary.items())
    for key, value in sorted_items:
        if key in model and model[key].get('type') == 'date':
            logger.info("Converting date value for key '%s' to human-readable format.", key)
            value = convert_date(value, get_system_locale())
        if not value:
            logger.warning("The value for key '%s' is empty.", key)
            value = 'the field is empty'

        print(f'{key}: {value}')


def sync_name(input_string):
    """
    Replace hyphens with underscores in the input string.

    :param input_string: The input string where hyphens need to be replaced.
    :return: The modified string with hyphens replaced by underscores.
    """
    logger.info("synch_name function was called")

    return input_string.replace('-', '_')
