"""
Provide start work with admin
Define entity and action
"""
import sys


def getopt_entity_action(argv):
    entity = sys.argv[1]
    action = sys.argv[2]
    args_entity_action = [entity, action]
    return args_entity_action

