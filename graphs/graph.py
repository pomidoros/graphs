from typing import Generic, TypeVar, List
from graphs.edge import Edge
from algorithms.short_distance_search import bfs, node_to_path


V = TypeVar("V")


class Graph(Generic[V]):
    def __init__(self, vertices: List[V] = []) -> None:
        self._vertices: List[V] = vertices
        self._edges: List[List[Edge]] = [[] for _ in vertices]

    @property
    def vertex_count(self) -> int:
        return len(self._vertices)

    @property
    def edges_count(self) -> int:
        return sum(map(len, self._edges))

    def add_vertex(self, vertex: V) -> None:
        self._vertices.append(vertex)
        self._edges.append([])

    def index_of(self, vertex: V) -> int:
        return self._vertices.index(vertex)

    def vertex_at(self, index: int) -> V:
        return self._vertices[index]

    def add_edge(self, edge: Edge) -> None:
        self._edges[edge.u].append(edge)
        self._edges[edge.v].append(edge.reverse())

    def add_edge_by_indices(self, u: int, v: int) -> None:
        edge = Edge(u, v)
        self.add_edge(edge)

    def add_edge_by_vertices(self, first, second) -> None:
        u = self.index_of(first)
        v = self.index_of(second)
        self.add_edge_by_indices(u, v)

    def neighbors_by_index(self, index: int) -> List[V]:
        return list(map(self.vertex_at, [el.v for el in self.edges_for_index(index)]))

    def neighbors_by_vertex(self, vertex: V) -> List[V]:
        index = self.index_of(vertex)
        return self.neighbors_by_index(index)

    def edges_for_index(self, index: int) -> List[Edge]:
        return self._edges[index]

    def edges_for_vertex(self, vertex: V) -> List[Edge]:
        return self._edges[self.index_of(vertex)]

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

    def __str__(self) -> str:
        string = ""
        for i in range(self.vertex_count):
            string += f"{self._vertices[i]} -> {self.neighbors_by_index(i)} \n"
        return string


if __name__ == "__main__":
    list_of_cites: List[str] = ["Seattle", "San Francisco", "Los Angeles", "Riverside", "Phoenix", "Chicago", "Boston",
                                "New York", "Atlanta", "Miami", "Dallas", "Houston", "Detroit", "Philadelphia",
                                "Washington"]
    city_graph = Graph(list_of_cites)
    city_graph.test_adding()
    # используем стандартный алгоритм поиска в ширину
    result_search = bfs("Boston", lambda x: x == "Miami", city_graph.neighbors_by_vertex)
    if result_search is not None:
        path = node_to_path(result_search)
        print(path)
    else:
        print("Haven't")
