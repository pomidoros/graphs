from typing import TypeVar, Callable, Optional, List, Generic, Deque, Set
from collections import deque


# type of cell
T = TypeVar('T')


class Queue(Generic[T]):
    def __init__(self):
        self._container: Deque[T] = deque([])

    def push(self, item) -> None:
        self._container.append(item)

    def pop(self) -> T:
        return self._container.popleft()

    @property
    def empty(self) -> bool:
        return not self._container

    def __repr__(self):
        return repr(self._container)


class Node(Generic[T]):
    def __init__(self, state: T, parent: Optional["Node"], cost: float = 0.0, heuristic: float = 0.0):
        self.state: T = state
        self.parent: Optional["Node"] = parent
        self.cost: float = cost
        self.heuristic: float = heuristic


def bfs(initial: T, goal_test: Callable[[T], bool], successors: Callable[[T], List[T]]) -> Optional[Node]:
    frontier: Queue[T] = Queue()
    added: Set[T] = {initial}
    frontier.push(Node(initial, None))
    while not frontier.empty:
        current_node: Node[T] = frontier.pop()
        current_state: T = current_node.state
        if goal_test(current_state):
            return current_node
        for child in successors(current_state):
            if child not in added:
                frontier.push(Node(child, current_node))
                added.add(child)
    return None


def node_to_path(node: Node) -> List[T]:
    path: List[T] = [node.state]
    while node.parent is not None:
        node = node.parent
        path.append(node.state)
    path.reverse()
    return path


if __name__ == "__main__":
    new_deque = Queue()
    new_deque.push(1)
    new_deque.push(2)
    new_deque.push(3)
    print(new_deque.pop())
    print(new_deque)


