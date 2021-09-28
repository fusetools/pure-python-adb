from abc import abstractmethod
from ppadb.connection import Connection
from typing import Any


class Command:
    @abstractmethod
    def create_connection(self, *args: Any, **kwargs: Any) -> Connection:
        raise NotImplementedError
