import logging
from abc import ABC, abstractmethod
from typing import Any, Dict


class AbsParserStrategy(ABC):
    """
    The Strategy interface declares operations common to all supported versions
    of Parser.

    The Context uses this interface to call the method defined by Concrete
    Strategies.
    """

    def __init__(self) -> None:
        self._logger = logging.getLogger(
            f"{__name__}.{self.__class__.__name__}",
        )

    @abstractmethod
    def execute(self, params: Dict[str, Any]):
        raise NotImplementedError
