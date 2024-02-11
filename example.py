import sys

from kraskal_algorithm import KruskalMST

graph = [
    [0, 22, 25, float('inf')],
    [22, 0, 13, 53],
    [25, 13, 0, 33],
    [float('inf'), 53, 33, 0]
]

kruskal = KruskalMST()
mst = kruskal.find_min_spanning_tree(graph)
print("Ребра минимального остовного дерева:", mst)