import pygame
from copy import deepcopy

class GUI:
  def __init__(self, maze, maze_solver, algorithm_name):
    self.maze = maze
    self.maze_solver = maze_solver
    self.algorithm = self.get_algorithm(algorithm_name)
    self.square_size = 50
    self.__screen = pygame.display.set_mode(
      [self.maze.width * self.square_size, self.maze.height * self.square_size]
    )
    self.running = True
    self.char_to_color = {
      '#': 'black',
      ' ': 'white',
      'X': 'brown1',
      'O': 'chartreuse3',
      'A': 'red',
      'B': 'green'
    }

  def launch(self):
    pygame.init()
    clock = pygame.time.Clock()
    solved = False
    while self.running:
      clock.tick(60)
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.running = False
      self.__screen.fill((255, 255, 255))

      if not solved:
          self.draw_maze()
          pygame.display.flip()
          solved_path = self.algorithm(self)
          solved = True
      self.draw_path(solved_path, True)
      pygame.display.flip()
    pygame.quit()

  def draw_maze(self):
    top_margin = 0
    for row in self.maze.list:
      left_margin = 0
      for char in row:
        self.draw_square(left_margin, top_margin, self.char_to_color[char])
        left_margin += self.square_size
      top_margin += self.square_size

  def draw_path(self, path, solved=False):
    for row, col in path:
      self.maze.list[row][col] = 'O' if solved else 'X'
    self.draw_maze()

  def draw_square(self, left_margin, top_margin, color):
    square = pygame.Rect(
      left_margin, top_margin, self.square_size, self.square_size
    )
    pygame.draw.rect(self.__screen, color, square)

  def get_algorithm(self, algorithm_name):
    algorithms = {
      'bfs': self.maze_solver.solve_with_bfs,
      'dfs': self.maze_solver.solve_with_dfs
    }
    return algorithms[algorithm_name]
