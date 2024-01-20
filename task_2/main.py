import networkx as nx
from graph_builder import GraphBuilder

SOURCE_NODE = "Hlavná Stanica"
TARGET_NODE = "Avion Shopping Park"

# Locations in Bratislava, Slovakia
locations = [
    ("Hlavná Stanica", (0, 0)),
    ("Špitálska Street", (2, 0)),
    ("Starý Most", (4, 0)),
    ("Bratislava Castle", (0, -2)),
    ("Main Square", (2, -2)),
    ("Apollo Bridge", (4, -2)),
    ("Petržalka", (0, -4)),
    ("Sad Janka Kráľa", (2, -4)),
    ("Incheba Expo", (4, -4)),
    ("Aupark", (0, -6)),
    ("Eurovea", (2, -6)),
    ("Železná Studienka", (4, -6)),
    ("Slavín", (0, -8)),
    ("Koliba", (2, -8)),
    ("Avion Shopping Park", (4, -8)),
]

# Approximate numbers in kilometers between locations
edges = [
    ("Hlavná Stanica", "Špitálska Street", 2),
    ("Hlavná Stanica", "Main Square", 2),
    ("Hlavná Stanica", "Bratislava Castle", 3),
    ("Špitálska Street", "Starý Most", 2),
    ("Špitálska Street", "Main Square", 2),
    ("Starý Most", "Bratislava Castle", 3),
    ("Starý Most", "Apollo Bridge", 3),
    ("Bratislava Castle", "Main Square", 2),
    ("Main Square", "Apollo Bridge", 5),
    ("Apollo Bridge", "Petržalka", 7),
    ("Apollo Bridge", "Sad Janka Kráľa", 5),
    ("Petržalka", "Sad Janka Kráľa", 5),
    ("Petržalka", "Aupark", 4),
    ("Sad Janka Kráľa", "Incheba Expo", 2),
    ("Sad Janka Kráľa", "Eurovea", 4),
    ("Incheba Expo", "Eurovea", 5),
    ("Aupark", "Eurovea", 3),
    ("Aupark", "Sad Janka Kráľa", 3),
    ("Eurovea", "Železná Studienka", 8),
    ("Eurovea", "Koliba", 6),
    ("Eurovea", "Slavín", 4),
    ("Železná Studienka", "Avion Shopping Park", 10),
    ("Železná Studienka", "Koliba", 4),
    ("Slavín", "Koliba", 5),
    ("Koliba", "Avion Shopping Park", 7),
]

bratislava_transportation_graph = GraphBuilder(locations, edges)

# DFS
dfs_path = bratislava_transportation_graph.get_dfs_path(SOURCE_NODE, TARGET_NODE)
print(
    f"\nDFS path from {SOURCE_NODE} to {TARGET_NODE}:\n",
    dfs_path,
)


# BFS
bfs_path = bratislava_transportation_graph.get_bfs_path(SOURCE_NODE, TARGET_NODE)
print(
    f"\nBFS path from {SOURCE_NODE} to {TARGET_NODE}:\n",
    bratislava_transportation_graph.get_bfs_path(SOURCE_NODE, TARGET_NODE),
)
