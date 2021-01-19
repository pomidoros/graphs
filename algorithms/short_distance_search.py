from typing import Optional, Callable, List, TypeVar, Generic, Set
from structures.queue import Queue

# далее приведёт оптимальный алгоритм, но в нашём случае type V означает название вершины
V = TypeVar('V')


# оболочка Node позволяет строить маршрут и запоминать родителей
class Node(Generic[V]):
    def __init__(self, state: V, parent: Optional["Node"]) -> None:
        self.state: V = state
        self.parent: Optional["Node"] = parent


def bfs(initial: V, goal_test: Callable[[V], bool], successors: Callable[[V], List[V]]) -> Optional[Node]:
    frontier: Queue[V] = Queue()
    added: Set[V] = {initial}
    frontier.push(Node(initial, None))
    while not frontier.empty:
        current_node: Node[V] = frontier.pop()
        current_state = current_node.state
        if goal_test(current_state):
            return current_node
        for child in successors(current_state):
            if child not in added:
                frontier.push(Node(child, current_node))
                added.add(child)
    return None


def node_to_path(node: Node[V]) -> List[V]:
    path: List[V] = [node.state]
    while node.parent is not None:
        node = node.parent
        path.append(node.state)
    path.reverse()
    return path
