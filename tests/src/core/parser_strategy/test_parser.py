from typing import Any, Dict

from src.core.parser_strategy.csv_strategy import CsvParserStrategy
from src.core.parser_strategy.parser import Parser
from src.protocols.parser_strategy import AbsParserStrategy


class MockParserStrategy(AbsParserStrategy):
    def __init__(self):
        super().__init__()
        self._vestings_by_employee = {}

    def execute(self, params: Dict[str, Any]):
        self._vestings_by_employee["EMPLOYEE_ID"] = {"ES001": {"ID": "fake-id"}}
        return True


class TestParserContext:
    def setup_method(self, function):
        """Setup before each function"""
        print('\n\n[+] Test: "{}"'.format(function.__name__))
        print("    " + function.__doc__)

    def test_parser_context_creation(self):
        """assert creation of a valid parser context with a valid concrete strategy"""
        parser = Parser(CsvParserStrategy())
        assert parser

    def test_execute_method_with_valid_params(self):
        """assert context execution method with a valid concrete strategy"""
        mock_strategy = MockParserStrategy()
        parser = Parser(mock_strategy)
        mock_params = {"fullfilename": "fake-file-name", "date": "2020-01-01"}
        parser.execute(mock_params)
        expected = {"ES001": {"ID": "fake-id"}}
        assert mock_strategy._vestings_by_employee["EMPLOYEE_ID"] == expected
