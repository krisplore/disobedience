#!venv/bin/python
"""
Serve as the main entry point for the service.
Handle command-line arguments, retrieve the entity and action,
and direct the program flow accordingly.
"""
from getopt_router import getopt_entity_action
from source.add import add as source_add


def main():
    """
    Main function of the service.

    This function retrieves the entity and action from command-line arguments
    and directs the program flow based on the provided entity and action.

    """
    args_entity_action: list = getopt_entity_action()
    entity: object = args_entity_action[0]
    action: object = args_entity_action[1]

    match entity:
        case 'source':
            source_add()
        case _:
            print('no')


if __name__ == "__main__":
    main()
