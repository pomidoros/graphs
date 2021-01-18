from typing import TypeVar, Generic, List, Optional
from edge import Edge
from search_algorithms import bfs, node_to_path, Node
import sys


T = TypeVar("T")  # type of graphs's vertex


class Graph(Generic[T]):
    def __init__(self, vertices: List[T] = []) -> None:
        self._vertices: List[T] = vertices
        self._edges: List[List[Edge]] = [[] for _ in self._vertices]

    # counts of vertices
    @property
    def vertex_count(self) -> int:
        return len(self._vertices)

    # count of edges
    @property
    def edge_count(self) -> int:
        return sum(map(len, self._edges))

    # add vertex to graph
    def add_vertex(self, vertex: T) -> None:
        self._vertices.append(vertex)
        self._edges.append([])
        return self.vertex_count - 1  # return index of added vertex

    # we should to add both edges because the graph is undirected
    def add_edge(self, edge: Edge) -> None:
        self._edges[edge.u].append(edge)
        self._edges[edge.v].append(edge.reversed())

    # add edge by indexes
    def add_edge_by_indices(self, u: int, v: int) -> None:
        edge = Edge(u, v)
        self.add_edge(edge)

    # add edge by names of vertices
    def add_edge_by_vertices(self, first: T, second: T) -> None:
        u = self._vertices.index(first)
        v = self._vertices.index(second)
        self.add_edge_by_indices(u, v)

    # return name of vertex by its index
    def vertex_at(self, ind: int) -> T:
        return self._vertices[ind]

    # return index of vertex by its name
    def index_of(self, vert: T) -> int:
        return self._vertices.index(vert)

    def neighbors_for_index(self, index: int) -> List[T]:
        return list(map(self.vertex_at, [e.v for e in self._edges[index]]))

    def neighbors_for_vertices(self, vertex: T) -> List[T]:
        index = self.index_of(vertex)
        return self.neighbors_for_index(index)

    def edges_for_index(self, index: int) -> List[Edge]:
        return self._edges[index]

    def edges_for_vertex(self, vertex: T) -> List[Edge]:
        return self.edges_for_index(self.index_of(vertex))

    def __str__(self) -> str:
        string = ""
        for i in range(self.vertex_count):
            string += f"{self.vertex_at(i)} -> {self.neighbors_for_index(i)} \n"
        return string

    def test_adding(self):
        self.add_edge_by_vertices("Seattle", "Chicago")
        self.add_edge_by_vertices("Seattle", "San Francisco")
        self.add_edge_by_vertices("Los Angeles", "Riverside")
        self.add_edge_by_vertices("Los Angeles", "Phoenix")
        self.add_edge_by_vertices("Riverside", "Phoenix")
        self.add_edge_by_vertices("Riverside", "Chicago")
        self.add_edge_by_vertices("Phoenix", "Dallas")
        self.add_edge_by_vertices("Phoenix", "Houston")
        self.add_edge_by_vertices("Houston", "Atlanta")
        self.add_edge_by_vertices("Houston", "Miami")
        self.add_edge_by_vertices("Atlanta", "Chicago")
        self.add_edge_by_vertices("Atlanta", "Washington")
        self.add_edge_by_vertices("Atlanta", "Miami")
        self.add_edge_by_vertices("Miami", "Washington")
        self.add_edge_by_vertices("Chicago", "Detroit")
        self.add_edge_by_vertices("Detroit", "Boston")
        self.add_edge_by_vertices("Detroit", "Washington")
        self.add_edge_by_vertices("Detroit", "New York")
        self.add_edge_by_vertices("Boston", "New York")
        self.add_edge_by_vertices("New York", "Philadelphia")
        self.add_edge_by_vertices("Philadelphia", "Washington")


if __name__ == "__main__":
    list_of_cites: List[str] = ["Seattle", "San Francisco", "Los Angeles", "Riverside", "Phoenix", "Chicago", "Boston",
                                "New York", "Atlanta", "Miami", "Dallas", "Houston", "Detroit", "Philadelphia",
                                "Washington"]
    new_graph: Graph[str] = Graph(list_of_cites)
    new_graph.test_adding()
    bfs_result: Optional[Node] = bfs("Boston", lambda x: x == "Miami", new_graph.neighbors_for_vertices)
    if bfs_result is None:
        print("Haven't")
    else:
        print(node_to_path(bfs_result))


