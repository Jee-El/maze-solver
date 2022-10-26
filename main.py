from maze import Maze
from graph import Graph
from maze_solver import MazeSolver


maze = Maze()
print(maze.hashtag_str, '\n\n')

width = maze.width
height = maze.height

print(maze.start, maze.end)
graph = Graph(maze, width, height)
adjacency_list = graph.adjacency_list

maze_solver = MazeSolver(maze, adjacency_list)
solved_path = maze_solver.solve()

maze.draw_path(solved_path)
