from itertools import product


class Graph:
    def __init__(self, maze, width, height):
        self.width = width
        self.height = height
        self.maze = maze
        self.vertices = tuple(
            product(range(0, height + 1), range(0, width + 1)))
        self.adjacency_list = self.build_adjacency_list()

    def build_adjacency_list(self, directions=((0, 1), (1, 0), (-1, 0), (0, -1))):
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
        return (0 <= row <= self.height) and (0 <= column <= self.width) and (self.maze.to_bool[row][column])
