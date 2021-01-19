from structures.abstract import Stack
from typing import List, TypeVar, Generic
from heapq import heappop, heappush


T = TypeVar('T')


class PriorityQueue(Generic[T], Stack):
    def __init__(self) -> None:
        super().__init__()
        self._container: List[T] = []

    def push(self, item: T) -> None:
        heappush(self._container, item)

    def pop(self) -> T:
        return heappop(self._container)
