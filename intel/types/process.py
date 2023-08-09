from intel.types.list_as_string import las_read, las_write


def read(data, model):
    for field, properties in model.items():
        field_type = properties.get('type')
        if field in data:
            value = data.get(field)
            match field_type:
                case 'list_as_string':
                    data[field] = las_read(value, properties)

    return data


def write(data, model):
    for field, properties in model.items():
        field_type = properties.get('type')
        if field in data:
            value = data.get(field)
            match field_type:
                case 'list_as_string':
                    data[field] = las_write(value, properties)

    return data
