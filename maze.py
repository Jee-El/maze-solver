from sty import fg, rs


class Maze:
    def __init__(self):
        maze_file = open('maze.txt')

        self.hashtag_maze = maze_file.read()

        maze_file.seek(0)

        maze_rows = [row.replace('\n', '') for row in maze_file.readlines()]

        maze_file.close()

        self.height = len(maze_rows) - 1
        self.width = len(maze_rows[0]) - 1

        self.bool_maze = self.bool_maze(maze_rows)

    def bool_maze(self, maze_rows):
        bool_maze = []
        for row in maze_rows:
            bool_row = []
            for char in row:
                bool_row.append(True if char == ' ' else False)
            bool_maze.append(bool_row)
        return bool_maze

    def draw_path(self, path):
        maze = []
        for row, col in path:
            self.bool_maze[row][col] = fg.red + 'X' + fg.rs
        for line in self.bool_maze:
            for char in line:
                if char == fg.red + 'X' + fg.rs:
                    maze.append(fg.red + 'X' + fg.rs)
                elif char:
                    maze.append(' ')
                else:
                    maze.append('#')
            maze.append('\n')
        print(''.join(maze))
