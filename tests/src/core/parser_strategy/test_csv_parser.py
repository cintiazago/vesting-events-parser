import pytest

from src.core.parser_strategy.csv_strategy import CsvParserStrategy
from src.types.event import Types


class TestCsvParser:
    def setup_method(self, function):
        """Setup before each function"""
        print('\n\n[+] Test: "{}"'.format(function.__name__))
        print("    " + function.__doc__)

    def test_is_target_date_higher_than_current_with_valid_params_returns_true(self):
        """assert if returns True in case target date is higher than current date"""

        csv_parser = CsvParserStrategy()

        mock_target_date = "2020-04-01"
        mock_current_date = "2020-01-01"
        result = csv_parser._is_target_date_higher_than_current(
            mock_target_date, mock_current_date
        )
        expected = True
        assert result == expected

    def test_is_target_date_higher_than_current_with_valid_params_returns_false(self):
        """
        assert if returns False in case target date is lower
        than current date
        """

        csv_parser = CsvParserStrategy()

        mock_target_date = "2020-01-01"
        mock_current_date = "2020-04-01"
        result = csv_parser._is_target_date_higher_than_current(
            mock_target_date, mock_current_date
        )
        expected = False
        assert result == expected

    def test_calc_total_quantity_to_vesting_event_with_event_of_type_vest(self):
        """assert the correct total quantity if the event type is VEST"""

        csv_parser = CsvParserStrategy()

        mock_event_type = Types.VEST
        mock_previous_quantity = 1000
        mock_current_quantity = 100
        result = csv_parser._calc_total_quantity_to_vesting_event(
            mock_event_type, mock_previous_quantity, mock_current_quantity
        )
        expected = 1100
        assert result == expected

    def test_calc_total_quantity_to_vesting_event_with_event_of_type_cancel(self):
        """assert the correct total quantity if the event type is CANCEL"""

        csv_parser = CsvParserStrategy()

        mock_event_type = Types.CANCEL
        mock_previous_quantity = 1000
        mock_current_quantity = 100
        result = csv_parser._calc_total_quantity_to_vesting_event(
            mock_event_type, mock_previous_quantity, mock_current_quantity
        )
        expected = 900
        assert result == expected

    def test_calc_total_quantity_to_vesting_event_trhows_with_event_of_type_unknown(
        self,
    ):
        """assert the correct total quantity if the event type is unknown"""

        csv_parser = CsvParserStrategy()

        mock_event_type = "unknown"
        mock_previous_quantity = 1000
        mock_current_quantity = 100
        with pytest.raises(TypeError):
            csv_parser._calc_total_quantity_to_vesting_event(
                mock_event_type, mock_previous_quantity, mock_current_quantity
            )

    def test_send_summary_notification_with_valid_object(self, capsys):
        """assert if the method sends the right notification message to stdout"""
        csv_parser = CsvParserStrategy()

        from pathlib import Path

        full_file_path = Path(__file__).parent

        mock_params = {
            "fullfilename": f"{full_file_path}/datamock.csv",
            "date": "2020-01-01",
            "precision": 2,
        }
        csv_parser.execute(mock_params)
        csv_parser._send_summary_notification()
        expeted = "E001,Alice Smith,ISO-001,0"

        out, _ = capsys.readouterr()
        assert expeted in out

    def test_execute_with_invalid_param_should_throw_key_error(self):
        """assert if the method throws a KeyError with invalid param"""
        csv_parser = CsvParserStrategy()
        mock_params = {"date": "2020-01-01", "precision": 2}

        with pytest.raises(KeyError):
            csv_parser.execute(mock_params)

    def test_execute_with_invalid_file_name_should_throw_os_error(self):
        """assert if the method throws a OSError with invalid filename"""
        csv_parser = CsvParserStrategy()
        mock_params = {
            "fullfilename": "invalid-filename.csv",
            "date": "2020-01-01",
            "precision": 2,
        }

        with pytest.raises(OSError):
            csv_parser.execute(mock_params)

    def test_execute_with_invalid_event_type_should_throw_type_error(self):
        """assert if the method throws a TypeError with invalid event type"""
        csv_parser = CsvParserStrategy()

        from pathlib import Path

        full_file_path = Path(__file__).parent
        mock_params = {
            "fullfilename": f"{full_file_path}/datamock_invalid_event.csv",
            "date": "2020-01-01",
            "precision": 2,
        }

        with pytest.raises(TypeError):
            csv_parser.execute(mock_params)

    def test_execute_with_invalid_file_structure_throw_an_error(self):
        """assert if the method throws an error with invalid file structure"""
        csv_parser = CsvParserStrategy()

        from pathlib import Path

        full_file_path = Path(__file__).parent
        mock_params = {
            "fullfilename": f"{full_file_path}/datamock_invalid_field.csv",
            "date": "2020-01-01",
            "precision": 2,
        }

        with pytest.raises(BaseException):
            csv_parser.execute(mock_params)
