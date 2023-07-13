"""
This module provides functions for determining characteristics of a source.
"""

import datetime         #
import secrets          #
import string           #
import uuid             #
from typing import Any
from intel.definitions import SOURCE_SCHEMA_VERSION, SOURCE_FIELDS_REQUIRED


AMOUNT_OF_INVITE: int = 2
INVITE_LENGTH: int = 7
EXCLUDED_CHARACTERS: str = 'B8CDO0QIJ1GS5'


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
    characters: list[str] = [c for c in alphabet if c not in EXCLUDED_CHARACTERS]
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

    creation_time = get_time()
    id_value = generate_id()

    source = {
        '_source_schema_version': SOURCE_SCHEMA_VERSION,
        'callsign': '',
        'tags': '',
        'invited by': '',
        'id': id_value,
        'type': set_type(),
        'reliability': 4.98,
        'note': 'some new note',
        'created': creation_time,
        'modified': creation_time,
        'invite': generate_invite(),
        'stats': {
            'total facts': 0,
            'confirmed facts': 0,
            'refuted facts': 0
        }
    }

    return source


def print_source_information(source):
    """
    Print the information contained in the source dictionary.

    Args:
        source (Dict[str, Any]): The source dictionary.
    """

    for key, value in source.items():
        print(f'{key}: {value}')


def validator(data_input: dict) -> dict:
    """
    Check if all required fields are present in the data dictionary and have non-empty values.

    :param data_input: A dictionary representing the questionnaire fields and values.
    :type data_input: dict

    :return: A dictionary with the result of the checks.
    :rtype: dict
    """

    result = {
        'status': True,
        'errors': {}
    }

    for field in SOURCE_FIELDS_REQUIRED:
        field_value = data_input.get(field)
        result['errors'][field] = []
        if field_value is None:
            result['errors'][field].append('empty')
            result['status'] = False
        elif field_value.strip() == '':
            result['errors'][field] = ['empty']
            result['status'] = False
        elif field not in data_input:
            result['errors'][field] = ['missing']
            result['status'] = False

    return result
