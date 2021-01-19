from graphs.edge import Edge
from dataclasses import dataclass


@dataclass
class WeightedEdge(Edge):
    weight: float

    def reverse(self) -> "WeightedEdge":
        return WeightedEdge(self.v, self.u, self.weight)

    def __repr__(self):
        return f"{self.u} --- {self.weight} --- {self.v}"

    def __lt__(self, other: "WeightedEdge") -> bool:
        return self.weight < other.weight
