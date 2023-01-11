import matplotlib.pyplot as plt
import networkx as nx
def draw_nodes(graph,nodes):
    for node in nodes:
        for k, v in node.items():
            if k=="name":
                name = v
                graph.add_node(v)
                break
    return graph
def draw_edges(graph,edges):
    for edge in edges:
        if edge :
            graph.add_edge(edge[0],edge[1])
    return graph


def draw_graph(graph):
    nx.draw_networkx(graph,with_labels=True)
    plt.show()