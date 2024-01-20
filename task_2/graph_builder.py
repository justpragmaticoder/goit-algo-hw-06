import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


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

    def get_dfs_path(self, source_node, target_node):
        result = []
        visited = set()
        stack = [source_node]
        while stack:
            vertex = stack.pop()

            if vertex not in visited:
                result.append(vertex)

                if vertex == target_node:
                    return result

                visited.add(vertex)

                neighbors = list(self.graph.neighbors(vertex))
                stack.extend(neighbors)
        return result

    def get_bfs_path(self, source_node, target_node):
        result = []
        visited = set()
        queue = deque([source_node])

        while queue:
            current_node = queue.popleft()

            if current_node not in visited:
                result.append(current_node)
                visited.add(current_node)

                neighbors = list(self.graph.neighbors(current_node))
                for neighbor in neighbors:
                    if neighbor not in visited:
                        queue.append(neighbor)
        return result
