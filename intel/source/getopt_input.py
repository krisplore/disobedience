import getopt
import sys


def parse_input_options(argv):
    """
    Parse command line arguments

    :param argv: list[str] of command line arguments.

    :return: A list of tuples representing the parsed options.
            Each tuples contains the option and argument.

    :rtype: list[tuple[str, str]]
    """
    try:
        opts, args = getopt.getopt(argv, "c:i:t:", ["callsign=", "invited_by=", "tags="])
    except getopt.GetoptError:  # invalid options - not c, i, t / if --option without argument
        print("Invalid options or missing required arguments")
        sys.exit(2)

    parsed_options = dict((opt, arg) for opt, arg in opts)
    print(type(parsed_options), parsed_options)

    return parsed_options



