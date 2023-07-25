#!venv/bin/python
"""
Serve as the main entry point for the service.
Handle command-line arguments, retrieve the entity and action,
and direct the program flow accordingly.
"""

import sys
from intel.getopt_router import getopt_entity_action
from intel.translation import start_translating
from intel.source.add import add as source_add

_ = start_translating()


def process_request(entity, action):
    """
    Process the request based on the provided entity and action.

    :param entity: str: The entity to perform the action on.
    :param action: str: The action to be performed on the entity.
    :return: The result of the action performed on the entity.
    """

    entities_actions = {
        'source': {
            'add': source_add,
            'edit': '',
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
            return entities_actions[entity][action]()
        print(_(f'Unknown action for {entity}'))
        sys.exit(2)
    else:
        print(_('No match for entity'))
        sys.exit(2)


def main():
    """
    Main function of the service.

    This function retrieves the entity and action from command-line arguments
    and directs the program flow based on the provided entity and action.
    """

    args_entity_action: list = getopt_entity_action()
    entity: object = args_entity_action[0]
    action: object = args_entity_action[1]

    process_request(entity, action)


if __name__ == "__main__":
    main()
