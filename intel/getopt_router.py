"""
Provide start work with admin
Define entity and action
"""

import sys

from intel.log import setup_logger

logger = setup_logger()


def getopt_entity_action():
    """
    Retrieves the entity and action arguments from the command line
    and returns a list containing them.

    Args:
        argv (list): A list of command line arguments.

    :return:A list containing the entity and action

    :rtype: list
    """
    logger.info("getopt_entity_action function was called")

    entity = sys.argv[1]
    action = sys.argv[2]
    args_entity_action = [entity, action]
    return args_entity_action
