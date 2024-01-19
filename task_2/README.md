We trying to compare behaviour of DFS and BFS algorithms on practice on Bratislava locations simulation.
Below you will find a result of work for each algorithm.

DFS_TREE paths from Hlavná Stanica to Avion Shopping Park:
('Hlavná Stanica', 'Špitálska Street')
('Špitálska Street', 'Starý Most')
('Starý Most', 'Bratislava Castle')
('Bratislava Castle', 'Main Square')
('Main Square', 'Apollo Bridge')
('Apollo Bridge', 'Petržalka')
('Petržalka', 'Sad Janka Kráľa')
('Sad Janka Kráľa', 'Incheba Expo')
('Incheba Expo', 'Aupark')
('Aupark', 'Eurovea')
('Eurovea', 'Železná Studienka')
('Železná Studienka', 'Slavín')
('Slavín', 'Koliba')
('Koliba', 'Avion Shopping Park')

BFS_TREE paths from Hlavná Stanica to Avion Shopping Park:
('Hlavná Stanica', 'Špitálska Street')
('Hlavná Stanica', 'Main Square')
('Hlavná Stanica', 'Bratislava Castle')
('Hlavná Stanica', 'Koliba')
('Špitálska Street', 'Starý Most')
('Špitálska Street', 'Incheba Expo')
('Main Square', 'Apollo Bridge')
('Koliba', 'Eurovea')
('Koliba', 'Slavín')
('Koliba', 'Avion Shopping Park')
('Incheba Expo', 'Sad Janka Kráľa')
('Incheba Expo', 'Aupark')
('Apollo Bridge', 'Petržalka')
('Eurovea', 'Železná Studienka')


Conclusion:
On practice you can see the major difference between DFS and BFS algorithms in action.
Depth-first search (DFS) is performed by visiting a vertex and then recursively visiting all neighboring vertices that have not yet been visited.
Breadth-breadth search (BFS) visits all vertices at a given level before proceeding to the next level.