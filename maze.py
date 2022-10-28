from sty import fg, rs
from copy import deepcopy


class Maze:
    def __init__(self, maze_file):
        self.hashtag_str = maze_file.read()

        maze_file.seek(0)

        self.hashtag_arr = self.hashtag_arr(maze_file)

        maze_file.close()

        self.to_bool = self.to_bool(self.hashtag_arr)
        self.border = self.border()

        self.height = len(self.hashtag_arr) - 1
        self.width = len(self.hashtag_arr[0]) - 1
        self.start, self.end = self.start_end()

    def to_bool(self, maze_rows):
        return [[True if char == ' ' else False for char in row] for row in maze_rows]

    def draw_path(self, path):
        hashtag_arr = deepcopy(self.hashtag_arr)

        self.draw_crosses(hashtag_arr, path)

        for row in hashtag_arr:
            print(''.join(row))

    def draw_crosses(self, maze, path):
        colored_cross = fg.red + 'X' + fg.rs
        for row, col in path:
            maze[row][col] = colored_cross

    def start_end(self):
        start, end = (), ()
        for i in range(len(self.border)):
            if i % 2:
                row_coordinate = i and self.height
            else:
                row_coordinate = i and self.width

            if start and end:
                return (start, end)
            if not start:
                start = (row_coordinate, self.border[i].index(True))
                continue
            if not end:
                end = (row_coordinate, self.border[i].index(True))

    def border(self):
        first_row = self.to_bool[0]
        last_row = self.to_bool[-1]
        first_col = [row[0] for row in self.to_bool]
        last_col = [row[-1] for row in self.to_bool]
        return (first_row, last_row, first_col, last_col)

    def hashtag_arr(self, maze_file):
        return [list(row.replace('\n', '')) for row in maze_file.readlines()]
