"""
The module contains a function for validating the type 'list_as_string'.
The check goes over the fields of the model.
"""


def validate_list_as_string(raw_source: dict, model: dict, result):
    """
    The function checks that the data matches the model by the length of the list
    and by the length of the elements of the given list.

    :param result: dictionary with status of validation
    :param model: dictionary of properties
    :param raw_source: dictionary of raw data that need to validated
    :return: dictionary with status of validation
    """

    for field, properties in model.items():
        if 'type' in properties and properties['type'] == 'list_as_string':
            value = raw_source.get(field)
            item_props = properties.get('item', {}).get('length', {})
            list_props = properties.get('length', {})

            if value is not None:
                if not isinstance(value, list):
                    value = [value]

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
                        item_len = len(item)
                        item_min, item_max = item_props.get('min'), item_props.get('max')
                        if item_min is not None and item_len < item_min:
                            result['status'] = False
                            result['errors'].append(f"Each item in field '{field}' must have length at least {item_min}.")
                        if item_max is not None and item_len > item_max:
                            result['status'] = False
                            result['errors'].append(f"Each item in field '{field}' must have length at most {item_max}.")

    return result


