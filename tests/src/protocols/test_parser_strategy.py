from typing import Any, Dict

import pytest

from src.protocols.parser_strategy import AbsParserStrategy


class MockParserStrategy(AbsParserStrategy):
    def __init__(self):
        super().__init__()

    def execute(self, params: Dict[str, Any]):
        return super().execute(params)


class TestAbsParserStrategy:
    def setup_method(self, function):
        """Setup before each function"""
        print('\n\n[+] Test: "{}"'.format(function.__name__))
        print("    " + function.__doc__)

    def test_instatiation_of_concrete_class_without_execute_method_implemented(self):
        """
        assert if strategy interface raises NotImplementedError
        when execute method is not implemented
        """
        with pytest.raises(NotImplementedError):
            mock_strategy = MockParserStrategy()
            mock_params = {"fullfilename": "fake-name", "date": "2020-01-01"}
            mock_strategy.execute(mock_params)
