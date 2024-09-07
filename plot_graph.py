import matplotlib.pyplot as plt
import networkx as nx


def undirected_graph(start: int, end: int, edges: list[list[int]]) -> None:
    plt.figure(figsize=(3, 2))
    G = nx.Graph()
    G.add_nodes_from(range(start, end + 1))
    G.add_edges_from(edges)
    pos = nx.spring_layout(G)
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color="lightblue",
        font_weight="bold",
        node_size=400,
        arrows=True,
    )

    plt.show()


n = 4
edges = [[0, 1], [0, 3], [1, 2], [1, 3]]
undirected_graph(0, 3, edges)
