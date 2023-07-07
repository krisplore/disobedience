"""
This module provides functions for determining characteristics of a source.
"""
import datetime         #
import secrets          #
import string           #
import uuid             #

AMOUNT_OF_INVITE = 2
INVITE_LENGTH = 7
EXCLUDED_CHARACTERS = 'B8CDO0QIJ1GS5'


def extract_tags(raw_tags):
    """
    Split a string by comma, remove spaces in the beginning and at the end of string.

    Arg:
       raw_tags (str): contain users tags separated by commas.

    :return: each of tags as separated element of list.
    :rtype: list.
    """
    tags = [item.strip() for item in raw_tags.split(',') if item.strip()]
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
    alphabet = string.ascii_uppercase + string.digits
    characters = [c for c in alphabet if c not in EXCLUDED_CHARACTERS]
    invite = []
    for _ in range(AMOUNT_OF_INVITE):
        token_bytes = secrets.token_bytes(INVITE_LENGTH)
        invite.append(''.join(characters[b % len(characters)] for b in token_bytes))
    return invite


def get_time():
    """
    Record the time the data was sent.

    :return: time of creation source data.
    :rtype: int
    """
    return int(datetime.datetime.now().timestamp())
