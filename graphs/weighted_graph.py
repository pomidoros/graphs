from typing import List, TypeVar, Generic, Tuple
from graphs.graph import Graph
from graphs.weighted_edge import WeightedEdge

V = TypeVar('V')


class WeightedGraph(Generic[V], Graph[V]):
    def __init__(self, vertices: List[V] = []) -> None:
        self._vertices: List[V] = vertices
        self._edges: List[List[WeightedEdge]] = [[] for _ in vertices]

    def add_edge_by_indices(self, u: int, v: int, weight: float) -> None:
        edge: WeightedEdge = WeightedEdge(u, v, weight)
        self.add_edge(edge)

    def add_edge_by_vertices(self, first: V, second: V, weight: float) -> None:
        u: int = self.index_of(first)
        v: int = self.index_of(second)
        self.add_edge_by_indices(u, v, weight)

    def neighbors_for_index_with_weight(self, index: int) -> List[Tuple[V, float]]:
        distance_tuples: List[Tuple[V, float]] = []
        for edge in self.edges_for_index(index):
            distance_tuples.append((self.vertex_at(edge.v), edge.weight))
        return distance_tuples

    def __str__(self) -> str:
        string: str = ""
        for i in range(self.vertex_count):
            string += f"{self.vertex_at(i)} -> {self.neighbors_for_index_with_weight(i)} \n"
        return string

    def test_adding(self):
        self.add_edge_by_vertices("Seattle", "Chicago", 1737)
        self.add_edge_by_vertices("Seattle", "San Francisco", 678)
        self.add_edge_by_vertices("San Francisco", "Riverside", 386)
        self.add_edge_by_vertices("San Francisco", "Los Angeles", 348)
        self.add_edge_by_vertices("Los Angeles", "Riverside", 50)
        self.add_edge_by_vertices("Los Angeles", "Phoenix", 357)
        self.add_edge_by_vertices("Riverside", "Phoenix", 307)
        self.add_edge_by_vertices("Riverside", "Chicago", 1704)
        self.add_edge_by_vertices("Phoenix", "Dallas", 887)
        self.add_edge_by_vertices("Phoenix", "Houston", 1015)
        self.add_edge_by_vertices("Dallas", "Chicago", 805)
        self.add_edge_by_vertices("Dallas", "Atlanta", 721)
        self.add_edge_by_vertices("Dallas", "Houston", 225)
        self.add_edge_by_vertices("Houston", "Atlanta", 702)
        self.add_edge_by_vertices("Houston", "Miami", 968)
        self.add_edge_by_vertices("Atlanta", "Chicago", 588)
        self.add_edge_by_vertices("Atlanta", "Washington", 543)
        self.add_edge_by_vertices("Atlanta", "Miami", 604)
        self.add_edge_by_vertices("Miami", "Washington", 923)
        self.add_edge_by_vertices("Chicago", "Detroit", 238)
        self.add_edge_by_vertices("Detroit", "Boston", 613)
        self.add_edge_by_vertices("Detroit", "Washington", 396)
        self.add_edge_by_vertices("Detroit", "New York", 482)
        self.add_edge_by_vertices("Boston", "New York", 190)
        self.add_edge_by_vertices("New York", "Philadelphia", 81)
        self.add_edge_by_vertices("Philadelphia", "Washington", 123)


if __name__ == "__main__":
    cities_list: List[str] = ["Seattle", "San Francisco", "Los Angeles", "Riverside", "Phoenix", "Chicago", "Boston",
                              "New York", "Atlanta", "Miami", "Dallas", "Houston", "Detroit", "Philadelphia",
                              "Washington"]
    city_graph: WeightedGraph[str] = WeightedGraph(cities_list)
    city_graph.test_adding()
    print(city_graph)
