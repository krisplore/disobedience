"""
Provide start work with admin
Define entity and action
"""
import logging
import sys

py_logger14 = logging.getLogger(__name__)
py_logger14.setLevel(logging.INFO)

py_handler = logging.FileHandler(f"logs/{__name__}.log", mode='w')
py_formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")

py_handler.setFormatter(py_formatter)
py_logger14.addHandler(py_handler)


def getopt_entity_action():
    """
    Retrieves the entity and action arguments from the command line
    and returns a list containing them.

    Args:
        argv (list): A list of command line arguments.

    :return:A list containing the entity and action

    :rtype: list
    """
    py_logger14.info("getopt_entity_action function was called")

    entity = sys.argv[1]
    action = sys.argv[2]
    args_entity_action = [entity, action]
    return args_entity_action
