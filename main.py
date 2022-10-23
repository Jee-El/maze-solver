from maze import Maze
from graph import Graph
from sty import fg, bg, ef, rs


def update_maze(char):
    if char == fg.red + 'X' + fg.rs:
        return char
    elif char:
        return ' '
    else:
        return '#'


m = Maze()
g = Graph(m)

p = g.path((0, 1), (10, 19))

for couple in p:
    g.maze[couple[0]][couple[1]] = fg.red + 'X' + fg.rs

solved_maze = list(map(lambda line: list(
    map(update_maze, line)), g.maze))
solved_maze = list(map(lambda line: ''.join(line), solved_maze))
solved_maze = "\n".join(solved_maze)
print(solved_maze)
