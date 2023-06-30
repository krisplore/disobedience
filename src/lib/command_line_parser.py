import getopt
import sys

REQUIRED_OPTIONS_SHORT = {"-c", "-i"}
REQUIRED_OPTIONS_FULL = {"--callsign", "--invited_by"}


def parse_command_line(argv):
    """
    Parse command line arguments

    :param argv: list[str] of command line arguments.

    :return: A list of tuples representing the parsed options.
            Each tuples contains the option and argument.

    :rtype: list[tuple[str, str]]
    """
    try:
        opts, args = getopt.getopt(argv, "c:i:t:", ["callsign=", "invited_by=", "tags="])
    except getopt.GetoptError:
        print("Invalid options or missing required arguments")
        sys.exit(2)

    entered_options = set(opt for opt, _ in opts)

    if not (REQUIRED_OPTIONS_SHORT.issubset(entered_options) or REQUIRED_OPTIONS_FULL.issubset(entered_options)):
        print("Not all required options entered")
        sys.exit(2)

    parsed_options = [(opt, arg) for opt, arg in opts]

    return parsed_options




