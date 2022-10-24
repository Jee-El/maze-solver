class MazeSolver:
    def __init__(self, maze, adjacency_list):
        self.maze = maze
        self.adjacency_list = adjacency_list

    def valid_coordinates(self, coordinates):
        row = coordinates[0]
        column = coordinates[1]
        if not (0 <= row <= self.maze.height):
            return False
        if not (0 <= column <= self.maze.width):
            return False
        if not (self.maze.bool_maze[row][column]):
            return False
        return True

    def solve(self, start, end):
        if not self.valid_coordinates(start) or not self.valid_coordinates(end):
            return print('Invalid Coordinates')
        if start == end:
            return end
        return self.bfs(start, end)

    def bfs(self, start, end):
        queue = [(start, [start])]
        visited = {start}

        while queue:
            vertex, path = queue.pop(0)
            if vertex == end:
                return path
            for adjacent_vertex in self.adjacency_list[vertex]:
                if adjacent_vertex in visited:
                    continue
                visited.add(adjacent_vertex)
                new_path = path + [adjacent_vertex]
                queue.append((adjacent_vertex, new_path))
        return []
