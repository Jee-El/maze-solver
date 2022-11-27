from maze import Maze
from graph import Graph
from maze_solver import MazeSolver
from time import sleep

nums_to_maze_fns = {
    '1': 'dfs_worst_case',
    '2': 'first_maze',
    '3': 'second_maze',
    '4': 'third_maze'
}

mazes_starts_ends = {
    'dfs_worst_case': ((6, 0), (5, 0)),
    'first_maze': ((0, 0), (10, 20)),
    'second_maze': ((0, 0), (20, 30)),
    'third_maze': ((0, 0), (64, 102))
}

def solve_maze(maze_fn):
    opened_maze_file = open(maze_fn + '.txt')

    maze = Maze(opened_maze_file, *mazes_starts_ends[maze_fn])

    print(maze.hashtag_str, '\n\n')
    sleep(1)

    width = maze.width
    height = maze.height

    graph = Graph(maze, width, height)
    adjacency_list = graph.adjacency_list

    maze_solver = MazeSolver(maze, adjacency_list)

    bfs_solved_path = maze_solver.solve_with_bfs() 
    maze.draw_path(bfs_solved_path)

    print('\n\n')

    dfs_solved_path = maze_solver.solve_with_dfs() 
    maze.draw_path(dfs_solved_path)

for num in nums_to_maze_fns:
    fn = nums_to_maze_fns[num]
    print(f'{num} : {fn}')

maze_to_solve = input('> Number : ')
while maze_to_solve not in nums_to_maze_fns:
    maze_to_solve = input('> Number : ')
    
solve_maze(nums_to_maze_fns[maze_to_solve])
