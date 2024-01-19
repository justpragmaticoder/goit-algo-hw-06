import networkx as nx
from graph_builder import GraphBuilder

SOURCE_NODE = "Hlavná Stanica"

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
    ("Špitálska Street", "Incheba Expo", 5),
    ("Starý Most", "Bratislava Castle", 3),
    ("Bratislava Castle", "Main Square", 2),
    ("Main Square", "Apollo Bridge", 5),
    ("Apollo Bridge", "Petržalka", 7),
    ("Apollo Bridge", "Sad Janka Kráľa", 5),
    ("Petržalka", "Sad Janka Kráľa", 5),
    ("Sad Janka Kráľa", "Incheba Expo", 2),
    ("Sad Janka Kráľa", "Eurovea", 4),
    ("Incheba Expo", "Aupark", 2),
    ("Aupark", "Eurovea", 3),
    ("Aupark", "Sad Janka Kráľa", 3),
    ("Aupark", "Avion Shopping Park", 5),
    ("Eurovea", "Železná Studienka", 8),
    ("Eurovea", "Koliba", 6),
    ("Železná Studienka", "Slavín", 6),
    ("Slavín", "Koliba", 5),
    ("Koliba", "Avion Shopping Park", 7),
    ("Koliba", "Slavín", 2),
    ("Koliba", "Hlavná Stanica", 6),
]

bratislava_transportation_graph = GraphBuilder(locations, edges)

shortest_paths = bratislava_transportation_graph.get_shortest_path_by_dijkstra(
    SOURCE_NODE
)

# Print the result from second item (because first location is SOURCE_NODE itself)
for node, distance in list(shortest_paths.items())[1:]:
    print(f"Shortest distance from {SOURCE_NODE} to {node}: {distance} kilometers")
