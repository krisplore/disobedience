

def validate_emptiness(value):
    """
    Check if the value is not None, not an empty string, and not containing only whitespace.

    :param value: The value to be checked.
    :type value: Any

    :return: True if the value is valid, False otherwise.
    :rtype: bool
    """

    return value is not None and value.strip() != ""
