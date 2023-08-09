"""
The module contains a functions for validating the type 'list_as_string'.
The check goes over the fields of the model.

Functions:
- validate_item_length
- validate_list
- validate_list_as_string
"""


def validate_item_length(field, item, item_props, result):
    """
    Validate the length of an item within a list.

    :param field: name of the field being validated
    :param result: dictionary with the results of the check
    :param item: item value to be validated.
    :param item_props: validation properties for the item.
    :return: dictionary with the results of the check
    """

    item_len = len(item)
    item_min, item_max = item_props.get('min'), item_props.get('max')

    if item_min is not None and item_len < item_min:
        result['status'] = False
        result['errors'].append(f"Each item in field '{field}' must have length at least {item_min}.")

    if item_max is not None and item_len > item_max:
        result['status'] = False
        result['errors'].append(f"Each item in field '{field}' must have length at most {item_max}.")

    return result


def validate_list(field, value, list_props, item_props, result):
    """
    Validate the list field.

    :param field: name of the field being validated
    :param value: value of the list field.
    :param list_props: validation properties for the list as a whole.
    :param item_props: validation properties for each item in the list.
    :param result: dictionary with the results of the check
    :return: dictionary with the results of the check
    """

    list_min, list_max = list_props.get('min'), list_props.get('max')

    if list_min is not None and len(value) < list_min:
        result['status'] = False
        result['errors'].append(f"Field '{field}' must have at least {list_min} items.")

    if list_max is not None and len(value) > list_max:
        result['status'] = False
        result['errors'].append(f"Field '{field}' must have at most {list_max} items.")

    for item in value:
        if not isinstance(item, str):
            result['status'] = False
            result['errors'].append(f"Invalid value for field '{field}'. Expected a string or a list.")
        else:
            result = validate_item_length(field, item, item_props, result)

    return result


def validate_list_as_string(raw_source: dict, model: dict, result: dict):
    """
    The function gets the maximum and minimum values for the length of the list and its elements.

    :param raw_source: dictionary with data to be checked
    :param model: dict of rules
    :param result: dictionary with the results of the check
    :return: dictionary with the results of the check
    """

    for field, properties in model.items():
        if 'type' in properties and properties['type'] == 'list_as_string':
            value = raw_source.get(field)
            item_props = properties.get('item', {}).get('length', {})
            list_props = properties.get('length', {})

            if value is not None:
                if not isinstance(value, list):
                    value = [value]

                validate_list(field, value, list_props, item_props, result)

    return result
