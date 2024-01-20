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

    def get_graph_characteristics(self):
        vertices_qty = len(self.graph.nodes())
        edges_qty = len(self.graph.edges())
        degree_of_vertices = dict(self.graph.degree())

        max_possible_edges = vertices_qty * (vertices_qty - 1) / 2
        graph_density = edges_qty / max_possible_edges

        return {
            "vertices_qty": vertices_qty,
            "edges_qty": edges_qty,
            "graph_density": graph_density,
            "degree_of_vertices": degree_of_vertices,
        }
