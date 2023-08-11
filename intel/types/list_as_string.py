from intel.logger import logger


def las_read(value, properties):
    separator = properties.get('separator', ',')
    if isinstance(value, str):
        value = [item.strip() for item in value.split(separator) if item.strip()]
        logger.debug('Data type "list_as_string" was written to list')
    return value


def las_write(value: list, properties):
    separator = properties.get('separator', ',')
    if isinstance(value, list):
        separator += " "
        value = separator.join(value)
        logger.debug('Data type "list_as_string" was written to string')

    return value


def validate():
    pass
