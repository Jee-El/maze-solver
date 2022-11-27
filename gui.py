import pygame
from copy import deepcopy

class GUI:
  def __init__(self, maze, maze_solver):
    self.maze = maze
    self.maze_solver = maze_solver
    self.square_size = 50
    self.__screen = pygame.display.set_mode(
      [self.maze.width * self.square_size, self.maze.height * self.square_size]
    )
    self.running = True
    self.char_to_color = {
      '#': 'black',
      ' ': 'white',
      'X': 'blue',
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
          solved_path = self.maze_solver.solve_with_bfs(self)
          solved = True
      self.draw_path(solved_path)
      pygame.display.flip()
    pygame.quit() 

  def draw_maze(self, maze):
    left_margin, top_margin = 0, 0
    for row in maze:
      for col in row:
        self.draw_square(left_margin, top_margin, self.char_to_color[col])
        left_margin += self.square_size
      left_margin = 0
      top_margin += self.square_size

  def draw_path(self, path):
    hashtag_arr = deepcopy(self.maze.hashtag_arr)
    for row, col in path:
      if hashtag_arr[row][col] == 'A' or hashtag_arr[row][col] == 'B':
        continue
      hashtag_arr[row][col] = 'X'
    self.draw_maze(hashtag_arr)

  def draw_square(self, left_margin, top_margin, color):
    square = pygame.Rect(
      left_margin, top_margin, self.square_size, self.square_size
    )
    pygame.draw.rect(self.__screen, color, square)
