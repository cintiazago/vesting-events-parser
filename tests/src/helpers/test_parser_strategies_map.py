from src.core.parser_strategy.csv_strategy import CsvParserStrategy
from src.helpers.parser_strategies_map import PARSER_STRATEGIES_MAPPER


class TestHelperParserStrategiesMap:
    def setup_method(self, function):
        """Setup before each function"""
        print('\n\n[+] Test: "{}"'.format(function.__name__))
        print("    " + function.__doc__)

    def test_parser_strategy_map_with_valid_file_extension(self):
        """
        assert if parser strategy map wil return a valid strategy
        with a valid file extension.
        """
        mock_stragety = "csv"
        strategy = PARSER_STRATEGIES_MAPPER.get(mock_stragety)
        assert type(strategy) == type(CsvParserStrategy())
