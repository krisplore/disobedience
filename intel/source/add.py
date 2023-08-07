"""
Responsible for managing the process of adding a new source.
"""
import logging
import sys

from intel.definitions import SOURCE_EXTENSION_YAML, PATH_TO_SOURCE_MODEL, ERR_BAD_OPTS
from intel.source.functions import create_stub, print_dictionary
from intel.source.load.file import parse_filename
from intel.source.load.method import parse_method_input
from intel.source.load.options import parse_options
from intel.source.validate.validator import validate
from intel.source.my_yaml import read, write
from intel.translation import start_translating

_ = start_translating()

py_logger2 = logging.getLogger(__name__)
py_logger2.setLevel(logging.INFO)

py_handler = logging.FileHandler(f"logs/{__name__}.log", mode='w')
py_formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")

py_handler.setFormatter(py_formatter)
py_logger2.addHandler(py_handler)


def add():
    """
    This function handles the process of adding a new data source.
    It prompts the user for required information, generates relevant data,
    and saves it to a file.
    """
    py_logger2.info("Add function started")
    print(_("Language"))

    source = create_stub()
    py_logger2.info("The stub for the source was created")

    method_input = parse_method_input()
    py_logger2.info("Input method defined")

    match method_input:
        case 'file':
            py_logger2.info("Case input method - file defined")
            raw_source = read(parse_filename(sys.argv[4:]))
        case 'opt':
            py_logger2.info("Case input method - options defined")
            raw_source = parse_options(sys.argv[4:])
        case _:
            py_logger2.error("Case input method not defined")
            print(_('Method does not exist'))
            sys.exit(ERR_BAD_OPTS)

    result = validate(raw_source, read(PATH_TO_SOURCE_MODEL + SOURCE_EXTENSION_YAML))

    if not result['status']:
        py_logger2.error("File validation failed")
        print(result)
        sys.exit(2)
    else:
        py_logger2.info("File validation completed successfully")

        print_dictionary(result, read(PATH_TO_SOURCE_MODEL + SOURCE_EXTENSION_YAML))
        py_logger2.info("The result was printed")

        source.update(raw_source)
        py_logger2.info("The raw source was merged into the stub source")

        write(source, source['id'])
        py_logger2.info("The source was written to a file")

        print_dictionary(source, read(PATH_TO_SOURCE_MODEL + SOURCE_EXTENSION_YAML))
        py_logger2.info("The source was printed")
