from intel.logger import logger
from intel.types.list_as_string import las_read, las_write


def read(data, model):
    for field, properties in model.items():
        field_type = properties.get('type')
        if field in data:
            value = data.get(field)
            match field_type:
                case 'list_as_string':
                    data[field] = las_read(value, properties)
                    logger.debug('Case match %s and "list_as_string" in read function', field_type)

    return data


def write(data, model):
    for field, properties in model.items():
        field_type = properties.get('type')
        if field in data:
            value = data.get(field)
            match field_type:
                case 'list_as_string':
                    data[field] = las_write(value, properties)
                    logger.debug('Case match %s and "list_as_string" in write function', field_type)

    return data
