from intel.types.list_as_string import read1, write1


def read(data, model):
    for field, properties in model.items():
        field_type = properties.get('type')
        value = data.get(field)
        separator = properties.get('separator', ',')
        match field_type:
            case 'list_as_string':
                data[field] = read1(value, separator)

    return data


def write(data, model):
    for field, properties in model.items():
        field_type = properties.get('type')
        value = data.get(field)
        separator = properties.get('separator', ',')
        match field_type:
            case 'list_as_string':
                data[field] = write1(value, separator)

    return data
