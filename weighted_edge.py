from typing import Generic, TypeVar, List
from edge import Edge
from dataclasses import dataclass


class WeightedEdge(Edge):
    weight: float

    def reversed(self) -> "WeightedEdge":
        return WeightedEdge(self.v, self.u, self.weight)

    def __lt__(self, other: "WeightedEdge") -> bool:
        return self.weight < other.weight

    def __str__(self):
        return f"{self.u} --- {self.weight} --- {self.v}"
