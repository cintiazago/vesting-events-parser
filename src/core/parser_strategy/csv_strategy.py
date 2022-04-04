from datetime import datetime
from typing import Any, Dict, Generator

from src.core.admin_notification import AdminNotification
from src.protocols.parser_strategy import AbsParserStrategy
from src.types.event import Columns, Types

"""
Concrete Strategies implement the algorithm while following the base Strategy
interface. The interface makes them interchangeable in the Context.
"""


class CsvParserStrategy(AbsParserStrategy):
    def __init__(self):
        super().__init__()
        self._vestings_by_employee = {}
        self._admin_notification = AdminNotification()
        self._precision = 2

    @staticmethod
    def _is_target_date_higher_than_current(target_date: str, date: str) -> bool:
        target_year, target_month, target_day = target_date.split("-")
        year, month, day = date.split("-")

        _target_date = datetime(int(target_year), int(target_month), int(target_day))

        _date = datetime(int(year), int(month), int(day))

        return _target_date >= _date

    @staticmethod
    def _calc_total_quantity_to_vesting_event(
        event: str, previous_quantity: float, current_quantity: float
    ) -> float:
        """
        Calculates the correct value for total quantity
        accondantly to the event type.
        """
        total_quantity = current_quantity
        if event == Types.VEST:
            total_quantity = previous_quantity + current_quantity
        elif event == Types.CANCEL:
            total_quantity = previous_quantity - current_quantity
        else:
            raise TypeError(f"Event type not found: {event}")
        return total_quantity

    def _send_summary_notification(self):
        self._logger.info("Sending notification...")

        for vesting in list(self._vestings_by_employee.keys()):
            current = self._vestings_by_employee[vesting]
            message = "{},{},{},{}".format(
                current["id"],
                current["name"],
                current["award_id"],
                current["total_quantity"],
            )
            self._admin_notification.notify_stdout(message)

    def _parse(self, target_date: str, data: Dict[str, str]):
        """Parse the given line to an object expected to the result.

        Given a target_date, if the record has the date higher then target_date
        it will not consider the record on the output.
        """
        current_quantity = float(data["QUANTITY"])
        total_quantity = current_quantity
        key = data["EMPLOYEE_ID"] + ":" + data["AWARD_ID"]
        employee = self._vestings_by_employee.get(key, "")
        event_type = data["EVENT"]
        if event_type not in [Types.VEST, Types.CANCEL]:
            raise TypeError(f"Event type not found: {event_type}")
        if employee:
            previous_quantity = employee["total_quantity"]
            total_quantity = self._calc_total_quantity_to_vesting_event(
                event_type, previous_quantity, current_quantity
            )
        total_quantity = (
            total_quantity
            if self._is_target_date_higher_than_current(target_date, data["DATE"])
            else 0
        )
        new_employee_summary = {
            "id": data["EMPLOYEE_ID"],
            "award_id": data["AWARD_ID"],
            "name": data["EMPLOYEE_NAME"],
            "total_quantity": round(total_quantity, self._precision),
        }
        self._vestings_by_employee[key] = new_employee_summary

    def _read_file_generator(self, full_file_name: str) -> Generator:
        """Reads the file and returns a generator."""
        self._logger.info(f"Reading file: {full_file_name}")
        lines = (line for line in open(full_file_name))
        list_line = (s.rstrip().split(",") for s in lines)
        vesting_dict = (dict(zip(Columns.DEFAULT, data)) for data in list_line)
        return vesting_dict

    def execute(self, params: Dict[str, Any]) -> None:
        """
        Orchestrate the execution of the Parser accordantly to the given parameters.
        """
        try:
            self._logger.info("Strategy is set to CSV Parser")
            self._precision = int(params["precision"])
            read_data_gen = self._read_file_generator(params["fullfilename"])
            for line in read_data_gen:
                self._parse(params["date"], line)
            self._send_summary_notification()
        except TypeError:
            raise
        except KeyError as err:
            self._logger.error(f"Param key not found: {err}")
            raise
        except OSError as err:
            self._logger.error(f"OS error: {err}")
            raise
        except BaseException as err:
            self._logger.error(f"Unexpected {err=}, {type(err)=}")
            raise
