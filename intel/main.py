#!venv/bin/python
"""
Serve as the main entry point for the service.
Handle command-line arguments, retrieve the entity and action,
and direct the program flow accordingly.
"""

import sys

from intel.definitions import ERR_DEFAULT
from intel.getopt_router import getopt_entity_action
from intel.log import logger_setup
from intel.source.add import add as source_add
from intel.translation import start_translating
from intel.source.edit import edit as source_edit

_ = start_translating()

logger = logger_setup()


def main():
    """
    Main function of the service.

    This function retrieves the entity and action from command-line arguments
    and directs the program flow based on the provided entity and action.
    """

    args_entity_action: list = getopt_entity_action()
    entity: object = args_entity_action[0]
    action: object = args_entity_action[1]
    logger.info("Entity and action parsed")
    route_request(entity, action)


def route_request(entity, action):
    """
    Process the request based on the provided entity and action.

    :param entity: str: The entity to perform the action on.
    :param action: str: The action to be performed on the entity.
    :return: The result of the action performed on the entity.
    """

    entities_actions = {
        'source': {
            'add': source_add,
            'edit': source_edit,
            'delete': '',
            'browse': ''
        },
        'fact': {
            'add': '',
            'edit': '',
            'delete': '',
            'browse': ''
        }
    }

    if entity in entities_actions:
        if action in entities_actions[entity]:
            logger.info("Entity and action defined")
            return entities_actions[entity][action]()
        logger.error("Action not defined")
        print(_(f'Unknown action for {entity}'))
        sys.exit(ERR_DEFAULT)
    else:
        logger.error("Entity not defined")
        print(_('No match for entity'))
        sys.exit(ERR_DEFAULT)


if __name__ == "__main__":
    main()
