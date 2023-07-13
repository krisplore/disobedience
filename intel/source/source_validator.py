from intel.definitions import SOURCE_FIELDS_REQUIRED


def validate(raw_source: dict) -> dict:
    """
    Check if all required fields are present in the data dictionary and have non-empty values.

    :param raw_source: A dictionary representing the questionnaire fields and values.
    :type raw_source: dict

    :return: A dictionary with the result of the checks.
    :rtype: dict
    """

    result = {
        'status': True,
        'errors': {}
    }

    for field in SOURCE_FIELDS_REQUIRED:
        field_value = raw_source.get(field)
        result['errors'][field] = []
        if field_value is None:
            result['errors'][field].append('empty')
            result['status'] = False
        elif field_value.strip() == '':
            result['errors'][field] = ['empty']
            result['status'] = False
        elif field not in raw_source:
            result['errors'][field] = ['missing']
            result['status'] = False

    return result
