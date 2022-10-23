from itertools import product


class Graph:
    def __init__(self, maze, width, height):
        self.width = width
        self.height = height
        self.vertices = list(
            product(range(0, height), range(0, width)))
        self.adjacency_list = self.build_adjacency_list(maze)

    def build_adjacency_list(self, maze, directions=[[0, 1], [1, 0], [-1, 0], [0, -1]]):
        adjacency_list = {}
        for vertex in self.vertices:
            adjacent_vertices = []
            for direction in directions:
                row = direction[0] + vertex[0]
                column = direction[1] + vertex[1]
                coordinates = row, column
                if not self.valid_coordinates(coordinates, maze):
                    continue
                adjacent_vertices.append(coordinates)
            adjacency_list[vertex] = adjacent_vertices
        return adjacency_list

    def valid_coordinates(self, coordinates, maze):
        row = coordinates[0]
        column = coordinates[1]
        return (0 <= column < self.width) and (0 <= row < self.height) and (maze.maze[row][column])
