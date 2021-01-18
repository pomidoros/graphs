from dataclasses import dataclass


@dataclass
class Edge:
    u: int
    v: int

    def __str__(self) -> str:
        return f"{self.u} -> {self.v}"

    def reversed(self) -> "Edge":
        return Edge(self.v, self.u)


if __name__ == "__main__":
    new_edge = Edge(1, 2)
    reversed_edge = new_edge.reversed()
    print(reversed_edge)
