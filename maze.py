from sty import fg, rs


class Maze:
    def __init__(self):
        self.height = 11
        self.width = 21
        self.construct_maze()

    def construct_maze(self):
        maze_txt = open('maze.txt')
        maze = list(map(lambda line: line.strip(), maze_txt.readlines()))
        maze_txt.close()

        self.maze = list(map(lambda line: list(
            map(lambda char: True if char == ' ' else False, line)), maze))

    def draw_path(self, path):
        maze = []
        for row, col in path:
            self.maze[row][col] = fg.red + 'X' + fg.rs
        for line in self.maze:
            for char in line:
                if char == fg.red + 'X' + fg.rs:
                    maze.append(fg.red + 'X' + fg.rs)
                elif char:
                    maze.append(' ')
                else:
                    maze.append('#')
            maze.append("\n")
        print(''.join(maze))

    def valid_coordinates(self, coordinates):
        row = coordinates[0]
        column = coordinates[1]
        return (0 <= column < self.width) and (0 <= row < self.height) and (self.maze[row][column])

    def path(self, start, end, adjacency_list):
        if not self.valid_coordinates(start) or not self.valid_coordinates(end):
            return print('Invalid Coordinates')
        if start == end:
            return end
        return self.bfs(start, end, adjacency_list)

    def bfs(self, start, end, adjacency_list):
        queue = [(start, [start])]
        visited = {start}

        while queue:
            vertex, path = queue.pop(0)
            if vertex == end:
                return path
            for adjacent_vertex in adjacency_list[vertex]:
                if adjacent_vertex in visited:
                    continue
                visited.add(adjacent_vertex)
                new_path = path + [adjacent_vertex]
                queue.append((adjacent_vertex, new_path))
