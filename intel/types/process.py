from intel.types.list_as_string import las_read, las_write


def read(data, model):
    for field, properties in model.items():
        field_type = properties.get('type')
        value = data.get(field)
        separator = properties.get('separator', ',')
        match field_type:
            case 'list_as_string':
                data[field] = las_read(value, separator)

    return data


def write(data, model):
    for field, properties in model.items():
        field_type = properties.get('type')
        value = data.get(field)
        separator = properties.get('separator', ',')
        match field_type:
            case 'list_as_string':
                data[field] = las_write(value, separator)

    return data
