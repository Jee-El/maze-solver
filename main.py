from maze import Maze
from graph import Graph
from maze_solver import MazeSolver


maze = Maze()
print(maze.hashtag_maze, '\n\n')

width = maze.width
height = maze.height

graph = Graph(maze, width, height)
adjacency_list = graph.adjacency_list

maze_solver = MazeSolver(maze, adjacency_list)
solved_path = maze_solver.solve((0, 0), (20, 30))

maze.draw_path(solved_path)
