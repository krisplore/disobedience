def las_read(value, separator):
    if isinstance(value, str):
        value = [item.strip() for item in value.split(separator) if item.strip()]

    return value


def las_write(value: list, separator):
    print(11, value)
    if isinstance(value, list):
        value = separator.join(value)

    return value


def validate():
    pass