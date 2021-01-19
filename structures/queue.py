from collections import deque
from structures.abstract import Stack
from typing import Generic, TypeVar, Deque

T = TypeVar('T')


class Queue(Stack, Generic[T]):
    def __init__(self):
        super().__init__()
        self._container: Deque[T] = deque([])

    def push(self, item: T) -> None:
        self._container.append(item)

    def pop(self) -> T:
        return self._container.popleft()

    @property
    def empty(self) -> bool:
        return not self._container

