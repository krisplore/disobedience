def las_read(value, properties):
    separator = properties.get('separator', ',')
    if isinstance(value, str):
        value = [item.strip() for item in value.split(separator) if item.strip()]

    return value


def las_write(value: list, properties):
    separator = properties.get('separator', ',')
    if isinstance(value, list):
        separator += " "
        value = separator.join(value)

    return value


def validate():
    pass
