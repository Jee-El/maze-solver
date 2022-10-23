from maze import Maze
from graph import Graph


maze = Maze()
width = maze.width
height = maze.height
graph = Graph(maze, width, height)
solution_path = maze.path((0, 1), (10, 19), graph.adjacency_list)
maze.draw_path(solution_path)
