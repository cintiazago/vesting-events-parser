import argparse
import logging.config

from src.core.parser_strategy.parser import Parser
from src.helpers.parser_strategies_map import PARSER_STRATEGIES_MAPPER


def config_log():
    logging.config.fileConfig(fname="logging.ini", disable_existing_loggers=False)


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-f",
        "--fullfilename",
        required=True,
        help="Full filename with path to be parsed",
    )
    parser.add_argument(
        "-d", "--date", required=True, help="Target date to filter the data"
    )
    parser.add_argument(
        "-p",
        "--precision",
        type=int,
        default=2,
        help="Set the precision value for decimals",
    )
    args = parser.parse_args()
    command_line_arguments = {key: value for key, value in vars(args).items() if value}
    return command_line_arguments


def main():
    config_log()
    kwargs = get_args()
    file_extension = kwargs["fullfilename"].split(".")[-1]

    parser = Parser(PARSER_STRATEGIES_MAPPER.get(file_extension))
    parser.execute(kwargs)


if __name__ == "__main__":
    main()
