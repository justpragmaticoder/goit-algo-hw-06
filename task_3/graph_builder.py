import networkx as nx
import matplotlib.pyplot as plt


class GraphBuilder:
    def __init__(self, nodes, edges):
        self.graph_structure = self.__convert_raw_edges_to_graph_structure(edges)
        self.graph = self.__build_graph(nodes, edges)

    def __build_graph(self, nodes, edges):
        graph = nx.Graph()

        for location, pos in nodes:
            graph.add_node(location, pos=pos)

        for edge in edges:
            graph.add_edge(edge[0], edge[1], weight=edge[2])

        return graph

    def __convert_raw_edges_to_graph_structure(self, edges):
        graph_structure = {}
        for edge in edges:
            source, target, weight = edge
            if source not in graph_structure:
                graph_structure[source] = {}

            if target not in graph_structure:
                graph_structure[target] = {}

            graph_structure[source][target] = weight
            graph_structure[target][source] = weight

        return graph_structure

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

    def get_shortest_path_by_dijkstra(self, start):
        # paths = {}
        distances = {vertex: float("infinity") for vertex in self.graph_structure}
        distances[start] = 0
        unvisited = list(self.graph_structure.keys())

        while unvisited:
            current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

            if distances[current_vertex] == float("infinity"):
                break

            for neighbor, weight in self.graph_structure[current_vertex].items():
                distance = distances[current_vertex] + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance

            unvisited.remove(current_vertex)

        return distances
