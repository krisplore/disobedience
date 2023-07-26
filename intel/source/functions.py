"""
This module provides functions for determining characteristics of a source.
"""

import datetime         #
import secrets          #
import string           #
import uuid             #
from typing import Any
from intel.definitions import SOURCE_SCHEMA_VERSION


AMOUNT_OF_INVITE: int = 2
INVITE_LENGTH: int = 7
CHARACTERS_FOR_EXCLUDE: str = 'B8CDO0QIJ1GS5'


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


def generate_invite():
    """
    Generate a list of unique invites.

    :return: list of invites, each of invite being a string.
    :rtype: list.
    """

    alphabet: str = string.ascii_uppercase + string.digits
    characters: list[str] = [c for c in alphabet if c not in CHARACTERS_FOR_EXCLUDE]
    invite = []
    for _ in range(AMOUNT_OF_INVITE):
        token_bytes: bytes = secrets.token_bytes(INVITE_LENGTH)
        invite.append(''.join(characters[b % len(characters)] for b in token_bytes))
    return invite


def get_time():
    """
    Record the time the data was sent.

    :return: time of creation source data.
    :rtype: int
    """

    return int(datetime.datetime.now().timestamp())


def create_source_stub():
    """
    Create an empty source dictionary with default values.

    Returns:
        Dict[str, Any]: The created source dictionary.
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
        'invite': generate_invite(),
        'stats': {
            'facts': {
                'total': 0,
                'confirmed': 0,
                'refuted': 0
            }
        }
    }

    return source


def print_dictionary(dictionary):
    """
    Print the information contained in the dictionary.

    Args:
        dictionary (Dict[str, Any]): The source dictionary.
    """

    for key, value in dictionary.items():
        print(f'{key}: {value}')
