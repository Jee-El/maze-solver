from sty import fg, rs
from copy import deepcopy


class Maze:
    def __init__(self, maze_file, start, end):
        self.start = start
        self.end = end

        self.hashtag_str = maze_file.read()

        maze_file.seek(0)

        self.hashtag_arr = self.hashtag_arr(maze_file)

        maze_file.close()

        self.to_bool = self.to_bool(self.hashtag_arr)

        self.height = len(self.hashtag_arr) - 1
        self.width = len(self.hashtag_arr[0]) - 1

    def to_bool(self, maze_rows):
        return [[True if char in [' ', 'A', 'B'] else False for char in row] for row in maze_rows]

    def draw_path(self, path):
        hashtag_arr = deepcopy(self.hashtag_arr)

        self.draw_crosses(hashtag_arr, path)

        for row in hashtag_arr:
            print(''.join(row))

    def draw_crosses(self, maze, path):
        for row, col in path:
            if maze[row][col] == 'A':
                maze[row][col] = fg.red + 'A' + fg.rs
            elif maze[row][col] == 'B':
                maze[row][col] = fg.green + 'B' + fg.rs
            else:
                maze[row][col] = fg.blue + 'X' + fg.rs

    def hashtag_arr(self, maze_file):
        return [list(row.replace('\n', '')) for row in maze_file.readlines()]
