from maze import Maze
from graph import Graph
from maze_solver import MazeSolver


def solve_maze(maze_file_name):

    maze = Maze(open(maze_file_name + '.txt'))

    print(maze.hashtag_str, '\n\n')

    width = maze.width
    height = maze.height

    graph = Graph(maze, width, height)
    adjacency_list = graph.adjacency_list

    maze_solver = MazeSolver(maze, adjacency_list)
    solved_path = maze_solver.solve()

    maze.draw_path(solved_path)


solve_maze('first_maze')

print('\n\n')

solve_maze('second_maze')
