from itertools import product

class Graph:
  def __init__(self, maze):
    self.maze = maze
    self.vertices = tuple(
      product(
        range(0, self.maze.height),
        range(0, self.maze.width)
      )
    )
    self.adjacency_list = self.build_adjacency_list()

  def build_adjacency_list(
    self, directions=((0, 1), (1, 0), (-1, 0), (0, -1))
    ):
    adjacency_list = {}
    for vertex in self.vertices:
      adjacent_vertices = []
      for direction in directions:
        row = direction[0] + vertex[0]
        column = direction[1] + vertex[1]
        coordinates = row, column
        if not self.are_valid_coordinates(coordinates):
          continue
        adjacent_vertices.append(coordinates)
      adjacency_list[vertex] = adjacent_vertices
    return adjacency_list

  def are_valid_coordinates(self, coordinates):
    row = coordinates[0]
    column = coordinates[1]
    return (
            (0 <= row < self.maze.height)
            and (0 <= column < self.maze.width)
            and (self.maze.bool_list[row][column])
    )
