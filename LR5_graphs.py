import matplotlib.pyplot as plt

import networkx
import random


# Создадим и выведем граф со списком ребер `(1,2),(1,3),(2,3), (2,4), (3,4)`:
edges_of_the_graph = [(1, 2), (1, 3), (2, 3), (2, 4), (3, 4)]
G = networkx.Graph(edges_of_the_graph)
plt.figure(figsize=(9, 7))
networkx.draw(G, with_labels=True, node_color='orange', edge_color='green')
plt.title("Граф с рёбрами `(1,2),(1,3),(2,3), (2,4), (3,4)`")
plt.show()

# Отобразим все базисные циклы:
graph_cube = networkx.hypercube_graph(3)
print("Базисные циклы:")
print(networkx.cycle_basis(graph_cube))

# Найдём все циклы в ориентированном графы:
edges_of_the_graph2 = [(0, 1),(1, 3), (1, 4), (4, 3), (2, 4), (3, 4),(1, 0)]
G2 = networkx.DiGraph(edges_of_the_graph2)
plt.figure(figsize=(7, 7))
networkx.draw(G2, with_labels=True, node_color='orange', edge_color='green')
plt.title("Граф")
plt.show()
print("Циклы в ориентированном графе:")
print(list(networkx.simple_cycles(G2)))

# Создадим случайный граф с 10 вершинами, в котором любая пара вершин соединена с вероятностью p=0.1
G3 = networkx.erdos_renyi_graph(10, 0.1)
plt.figure(figsize=(7, 7))
networkx.draw(G3, with_labels=True, node_color='orange', edge_color='green')
plt.title("Случайный граф")
plt.show()

# Создадим 1000 случайных графов с 100 узлами и построим график размера наибольшей компоненты связности:
Ps = []
connectivity_components = []
for _ in range(1000):
    p = random.uniform(0.005, 0.03)
    G4 = networkx.erdos_renyi_graph(100, p)
    connectivity_components.append(len(max(networkx.connected_components(G4), key=len)))
    Ps.append(p)
plt.figure(figsize=(9, 7))
plt.scatter(Ps, connectivity_components, color='green')
plt.xlabel("Вероятность")
plt.ylabel("Наибольшая компонента связности")
plt.title("Случайные графы")
plt.show()






