import networkx as nx
import matplotlib.pyplot as plt


class GraphBuilder:
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges
        self.__build_graph()

    def __build_graph(self):
        self.graph = nx.Graph()

        for location, pos in self.nodes:
            self.graph.add_node(location, pos=pos)

        for edge in self.edges:
            self.graph.add_edge(edge[0], edge[1], weight=edge[2])

    def draw_graph(self):
        pos = nx.get_node_attributes(self.graph, "pos")
        nx.draw(
            self.graph,
            pos,
            with_labels=True,
            font_weight="bold",
            node_size=700,
            node_color="skyblue",
            font_color="black",
            font_size=5,
        )
        labels = nx.get_edge_attributes(self.graph, "weight")
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=labels)

        plt.show()
