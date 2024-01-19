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

    def __find_paths(self, graph, algorithm, source, target):
        path_tree = algorithm(graph, source=source)
        path_edges = list(path_tree.edges())

        print(f"\n{algorithm.__name__.upper()} paths from {source} to {target}:")
        for path_edge in path_edges:
            print(path_edge)

        return path_edges

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

    def get_dfs_path(self, source_node, target_node):
        return self.__find_paths(self.graph, nx.dfs_tree, source_node, target_node)

    def get_bfs_path(self, source_node, target_node):
        return self.__find_paths(self.graph, nx.bfs_tree, source_node, target_node)
