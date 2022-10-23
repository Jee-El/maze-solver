from itertools import product


class Graph:
    def __init__(self, maze):
        self.maze = maze.maze
        self.width = maze.width
        self.height = maze.height
        self.vertices = list(
            product(range(0, self.height), range(0, self.width)))
        self.adjacency_list = self.build_adjacency_list(maze.directions)

    def build_adjacency_list(self, directions):
        adjacency_list = {}
        for vertex in self.vertices:
            adjacent_vertices = []
            for direction in directions:
                row = direction[0] + vertex[0]
                column = direction[1] + vertex[1]
                coordinates = row, column
                if not self.valid_coordinates(coordinates):
                    continue
                adjacent_vertices.append(coordinates)
            adjacency_list[vertex] = adjacent_vertices
        return adjacency_list

    def valid_coordinates(self, coordinates):
        row = coordinates[0]
        column = coordinates[1]
        return (0 <= column < self.width) and (0 <= row < self.height) and (self.maze[row][column])

    def path(self, start, end):
        if not self.valid_coordinates(start) or not self.valid_coordinates(end):
            return print('invalid')
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
