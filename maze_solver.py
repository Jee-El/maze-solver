from os import system
from time import sleep
import pygame

class MazeSolver:
  def __init__(self, maze, adjacency_list):
    self.maze = maze
    self.adjacency_list = adjacency_list
    self.dfs_explored_states = 0
    self.bfs_explored_states = 0

  def are_valid_coordinates(self, coordinates):
    row = coordinates[0]
    column = coordinates[1]
    if (
        not (0 <= row < self.maze.height)
        or not (0 <= column < self.maze.width)
        or not (self.maze.to_bool[row][column])
      ):
      print('>> Invalid Coordinates')
      return False
    return True

  def solve_with_bfs(self, gui):
    start = self.maze.start
    end = self.maze.end

    for coordinates in (start, end):
      if not self.are_valid_coordinates(coordinates):
        return

    return self.__bfs(gui, start, end)

  def solve_with_dfs(self, gui):
    start = self.maze.start
    end = self.maze.end

    for coordinates in (start, end):
      if not self.are_valid_coordinates(coordinates):
        return

    return self.__dfs(start, end, [(start, [start])], {start})

  def __bfs(self, gui, start, end):
    queue = [(start, [start])]
    visited_vertices = {start}

    while queue:
      vertex, path = queue.pop(0)
      self.bfs_explored_states += 1

      gui.draw_path(path)
      pygame.display.flip()
      while self.enter_is_not_pressed():
        pass

      if vertex == end:
        print(f'Explored states: {self.bfs_explored_states}')
        self.bfs_explored_states = 0
        return path

      for adjacent_vertex in self.adjacency_list[vertex]:
        if adjacent_vertex in visited_vertices:
          continue
        visited_vertices.add(adjacent_vertex)
        new_path = path + [adjacent_vertex]
        queue.append((adjacent_vertex, new_path))
    raise Exception('No Solution')

  def __dfs(
    self, gui, start, end, queue, visited_vertices, explored_states = 0
    ):
    if not queue:
      raise Exception('No Solution')
      
    vertex, path = queue.pop(0)
    self.dfs_explored_states += 1

    gui.draw_path(path)
    pygame.display.flip()
    while self.enter_is_not_pressed():
      pass

    if vertex == end:
      print(f'Explored states: {self.dfs_explored_states}')
      self.dfs_explored_states = 0
      return path

    for adjacent_vertex in self.adjacency_list[vertex]:
      if adjacent_vertex in visited_vertices:
        continue
      visited_vertices.add(adjacent_vertex)
      new_path = path + [adjacent_vertex]
      new_queue = queue + [(adjacent_vertex, new_path)]
      solved_path = self.__dfs(start, end, new_queue, visited_vertices, explored_states)

      if solved_path:
        return solved_path

  def enter_is_not_pressed(self):
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RETURN:
          return False
    return True
