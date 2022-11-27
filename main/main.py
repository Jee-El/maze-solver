from gui import GUI
from maze import Maze
from graph import Graph
from maze_solver import MazeSolver

def solve_maze(maze_fn, algorithm_name):
  opened_maze_file = open(maze_fn + '.txt')
  maze = Maze(opened_maze_file)
  graph = Graph(maze)
  adjacency_list = graph.adjacency_list
  maze_solver = MazeSolver(maze, adjacency_list)
  GUI(maze, maze_solver, algorithm_name).launch()

def display_options(nums_to_maze_fns):  
  for num in nums_to_maze_fns:
    fn = nums_to_maze_fns[num]
    print(f'{num} : {fn}')

def get_maze(nums_to_maze_fns):
  str_num = input('> Number : ')
  while str_num not in nums_to_maze_fns:
    str_num = input('> Number : ')
  return nums_to_maze_fns[str_num]

def get_algorithm_name(str_nums_to_algorithm_names):
  str_num = input('> Number : ')
  while str_num not in str_nums_to_algorithm_names:
    algorithm = input('1 -> BFS\n2 -> DFS')
  return str_nums_to_algorithm_names[str_num]

str_nums_to_maze_fns = {
  '1': 'dfs_worst_case',
  '2': 'bfs_worst_case',
  '3': 'third_maze',
  '4': 'fourth_maze'
}

str_nums_to_algorithm_names = {
    '1': 'bfs',
    '2': 'dfs'
}

display_options(str_nums_to_maze_fns)
maze_to_solve = get_maze(str_nums_to_maze_fns)

display_options(str_nums_to_algorithm_names)
algorithm_name = get_algorithm_name(str_nums_to_algorithm_names)

solve_maze(maze_to_solve, algorithm_name)
