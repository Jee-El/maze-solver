from gui import GUI
from maze import Maze
from graph import Graph
from maze_solver import MazeSolver


def solve_maze(maze_fn, algo_name):
    maze_file = open(maze_fn + ".txt")
    maze = Maze(maze_file)
    graph = Graph(maze)
    adjacency_list = graph.adjacency_list
    maze_solver = MazeSolver(maze, adjacency_list)
    GUI(maze, maze_solver, algo_name).launch()


def display_menu(menu: dict):
    for key, value in menu.items():
        print(key, value, sep=" : ")


def get_maze(maze_fns: dict):
    str_num = input("> Number : ")
    while str_num not in maze_fns:
        str_num = input("> Number : ")
    return maze_fns[str_num]


def get_algo_name(algo_names: dict):
    str_num = input("> Number : ")
    while str_num not in algo_names:
        str_num = input("> Number : ")
    return algo_names[str_num]


maze_fns = {
    "1": "dfs_worst_case",
    "2": "bfs_worst_case",
    "3": "third_maze",
    "4": "fourth_maze",
}

algo_names = {"1": "dfs", "2": "bfs", "3": "gbfs"}

display_menu(maze_fns)
maze_to_solve = get_maze(maze_fns)

display_menu(algo_names)
algorithm_name = get_algo_name(algo_names)

solve_maze(maze_to_solve, algorithm_name)
