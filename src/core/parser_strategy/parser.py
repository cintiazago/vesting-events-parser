from __future__ import annotations

import logging
from typing import Any, Dict

from src.protocols.parser_strategy import AbsParserStrategy


class Parser:
    """
    The Context defines the interface of interest to clients.
    """

    def __init__(self, strategy: AbsParserStrategy) -> None:
        """
        The Context accepts a strategy through the constructor, but
        also provides a setter to change it at runtime.
        """
        self._strategy = strategy
        self._logger = logging.getLogger(__name__)

    def execute(self, params: Dict[str, Any]) -> None:
        """
        The Context delegates some work to the Strategy object instead of
        implementing multiple versions of the algorithm on its own.
        """
        self._logger.info("Parsing data using the strategy (not sure how it'll do it)")
        result = self._strategy.execute(params)
        if result:
            self._logger.info("Execution finished successfully")
