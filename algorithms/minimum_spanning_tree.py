# рёбра хранятся в очереди с приоритетом
from structures.priority import PriorityQueue
from typing import List, Optional, TypeVar
# рёбра - взвешанные
from graphs.weighted_edge import WeightedEdge
# работаем со взвешанным графом
from graphs.weighted_graph import WeightedGraph

V = TypeVar('V')
# псевдоним для типизации
WeightedPath = List[WeightedEdge]


# функция для поиска общего веса пути дерева
def total_weight(path: WeightedPath) -> float:
    return sum([edge.weight for edge in path])


# minimum spanning tree
def mst(wg: WeightedGraph, start: int = 0) -> Optional[WeightedPath]:
    # путь
    result: WeightedPath = []
    # иницализируем все вершины как непросмотренные
    visited: List[bool] = [False] * wg.vertex_count
    # создаём очередь с приоритетом для всех вершин
    pq: PriorityQueue[WeightedEdge] = PriorityQueue()

    # встроенная фунция. вызываем при добавлении пути к новой вершине
    def visit(index: int):
        # отмечаем подходящую вершину как добавленную
        visited[index] = True
        # Добавляем в очередь все ребра, подходящие для просмотра
        for edge in wg.edges_for_index(index):
            if visited[edge.v]:
                continue
            pq.push(edge)

    # добавляем самую первую вершину
    visit(start)

    # пока что-то есть в очереди
    while not pq.empty:
        # получаем ребро с наименьшей длиной
        edge = pq.pop()
        # если она соединяет с уже добавленным ребром - пропускаем
        if visited[edge.v]:
            continue
        # иначе добавляем её в путь
        result.append(edge)
        # получаем новые пути для добавления
        visit(edge.v)

    return result


# выводим все пути и их общую стоимость
def print_weighted_path(wg: WeightedGraph, wp: WeightedPath):
    for edge in wp:
        print(f"{wg.vertex_at(edge.u)} -- {edge.weight} -- {wg.vertex_at(edge.v)}")
    print(f"{total_weight(wp)}")


if __name__ == "__main__":
    cities_list: List[str] = ["Seattle", "San Francisco", "Los Angeles", "Riverside", "Phoenix", "Chicago", "Boston",
                              "New York", "Atlanta", "Miami", "Dallas", "Houston", "Detroit", "Philadelphia",
                              "Washington"]
    # создаём граф
    weighted_graph: WeightedGraph = WeightedGraph(cities_list)
    # генерируем пути
    weighted_graph.test_adding()
    # применяем алгоритм Ярника (минимизации остовного дерева)
    weighted_path = mst(weighted_graph)
    if weighted_path is not None:
        print_weighted_path(weighted_graph, weighted_path)
    else:
        print("Haven't")
