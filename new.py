from dataclasses import dataclass


@dataclass
class Edge:
    u: int
    v: int

    def __str__(self):
        return f"{self.u} -> {self.v}"


obj = Edge(1, 2)
print(obj)
