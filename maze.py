from itertools import product


class Maze:
    def __init__(self):
        self.directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        self.height = 11
        self.width = 21
        self.maze = self.construct_maze()

    def construct_maze(self):
        maze_txt = open('maze.txt')
        maze = list(map(lambda line: line.strip(), maze_txt.readlines()))

        maze_txt.close()
        return list(map(lambda line: list(
            map(lambda char: True if char == ' ' else False, line)), maze))
