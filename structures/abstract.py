from abc import ABC, abstractmethod
from typing import List, Generic, TypeVar

T = TypeVar('T')


class Stack(ABC, Generic[T]):
    @abstractmethod
    def __init__(self) -> None:
        self._container: List[T] = []

    @abstractmethod
    def pop(self) -> T:
        pass

    @abstractmethod
    def push(self, item: T) -> None:
        pass

    @property
    def empty(self) -> bool:
        return not self._container
