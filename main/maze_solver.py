import pygame

class MazeSolver:
  def __init__(self, maze, adjacency_list):
    self.maze = maze
    self.adjacency_list = adjacency_list
    self.dfs_explored_states = 0
    self.bfs_explored_states = 0

  def solve_with_bfs(self, gui):
    start = self.maze.start
    end = self.maze.end
    solution = self.__bfs(gui, start, end)
    return solution or self.__no_solution_found()

  def solve_with_dfs(self, gui):
    start = self.maze.start
    end = self.maze.end
    solution = self.__dfs(gui, start, end, [(start, [start])], {start})
    return solution or self.__no_solution_found()

  def __bfs(self, gui, start, end):
    queue = [(start, [start])]
    visited_vertices = {start}

    while queue:
      vertex, path = queue.pop(0)
      self.bfs_explored_states += 1

      while self.__enter_is_not_pressed():
        pass
      gui.draw_path(path)
      pygame.display.flip()

      if vertex == end:
        print('Explored states : ', self.bfs_explored_states)
        return path

      for adjacent_vertex in self.adjacency_list[vertex]:
        if adjacent_vertex not in visited_vertices:
          visited_vertices.add(adjacent_vertex)
          new_path = path + [adjacent_vertex]
          queue.append((adjacent_vertex, new_path))
  
  def __dfs(self, gui, start, end, queue, visited_vertices):      
    vertex, path = queue.pop(0)
    self.dfs_explored_states += 1

    while self.__enter_is_not_pressed():
      pass
    gui.draw_path(path)
    pygame.display.flip()

    if vertex == end:
      print('Explored states : ', self.dfs_explored_states)
      return path

    for adjacent_vertex in self.adjacency_list[vertex]:
      if adjacent_vertex not in visited_vertices:
        visited_vertices.add(adjacent_vertex)
        new_path = path + [adjacent_vertex]
        new_queue = queue + [(adjacent_vertex, new_path)]
        solved_path = self.__dfs(gui, start, end, new_queue, visited_vertices)

        if solved_path:
          return solved_path

  def __enter_is_not_pressed(self):
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RETURN:
          return False
    return True

  def __no_solution_found(self):
    raise Exception('No Solution was found')
