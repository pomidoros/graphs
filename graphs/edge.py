from dataclasses import dataclass


@dataclass
class Edge:
    u: int
    v: int

    def reverse(self) -> "Edge":
        return Edge(self.v, self.u)

    def __repr__(self):
        return f"{self.u} -> {self.v}"
