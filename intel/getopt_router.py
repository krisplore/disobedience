"""
Provide start work with admin
Define entity and action
"""

import sys

from intel.logger import logger


def getopt_entity_action():
    """
    Retrieves the entity and action arguments from the command line
    and returns a list containing them.

    Args:
        argv (list): A list of command line arguments.

    :return:A list containing the entity and action

    :rtype: list
    """

    entity = sys.argv[1]
    action = sys.argv[2]
    args_entity_action = [entity, action]
    if args_entity_action:
        logger.debug("Entity and action were parsed")

    return args_entity_action
