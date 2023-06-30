import getopt
import sys


def parse_command_line(argv):
    try:
        opts, args = getopt.getopt(argv, "c:i:t:", ["callsign=", "invited_by=", "tags="])
    except getopt.GetoptError:
        print("Invalid options or missing required arguments")
        sys.exit(2)

    required_options_short = {"-c", "-i"}
    required_options_full = {"--callsign", "--invited_by"}
    entered_options = set(opt for opt, _ in opts)

    if not (required_options_short.issubset(entered_options) or required_options_full.issubset(entered_options)):
        print("Not all required options entered")
        sys.exit(2)

    parsed_options = [(opt, arg) for opt, arg in opts]

    return parsed_options




