import logging
from abc import ABC, abstractmethod


class AbsNotification(ABC):
    def __init__(self) -> None:
        self._logger = logging.getLogger(
            f"{__name__}.{self.__class__.__name__}",
        )

    @abstractmethod
    def notify_stdout(self, message: str):
        raise NotImplementedError
