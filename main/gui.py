import pygame

class GUI:
  def __init__(self, maze, maze_solver, algorithm_name):
    self.maze = maze
    self.maze_solver = maze_solver
    self.algorithm = self.get_algorithm(algorithm_name)
    self.square_size = 50
    pygame.display.set_caption('Maze Solver by Jee El')
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
    self.font = pygame.font.SysFont('Arial', 25)
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
      self.draw_path(solved_path, solved=True)
      self.running = False
      pygame.display.flip()
    pygame.quit()

  def draw_maze(self, is_gbfs=False):
    top_margin = 0
    for i in range(len(self.maze.list)):
      left_margin = 0
      for j in range(len(self.maze.list[i])):
        char = self.maze.list[i][j]
        self.draw_square(left_margin, top_margin, self.char_to_color[char])
        if is_gbfs:
          manhattan_distance = self.get_manhattan_distance((i, j), self.maze.end)
          self.draw_manhattan_distance(left_margin, top_margin, manhattan_distance)
        left_margin += self.square_size
      top_margin += self.square_size

  def draw_path(self, path, is_gbfs=False, solved=False):
    for row, col in path:
      self.maze.list[row][col] = 'O' if solved else 'X'
    self.draw_maze(is_gbfs)

  def draw_square(self, left_margin, top_margin, color):
    square = pygame.Rect(
      left_margin, top_margin, self.square_size, self.square_size
    )
    pygame.draw.rect(self.__screen, color, square)

  def draw_manhattan_distance(self, left_margin, top_margin, manhattan_distance):
    text = self.font.render(str(manhattan_distance), True, (0, 0, 0))
    left_margin += (self.square_size - text.get_width()) / 2
    top_margin += (self.square_size - text.get_height()) / 2
    self.__screen.blit(text, (left_margin, top_margin))

  def get_algorithm(self, algorithm_name):
    algorithms = {
      'dfs': self.maze_solver.solve_with_dfs,
      'bfs': self.maze_solver.solve_with_bfs,
      'gbfs': self.maze_solver.solve_with_gbfs
    }
    return algorithms[algorithm_name]
  
  def get_manhattan_distance(self, start, end):
    return abs(start[0] - end[0]) + abs(start[1] - end[1])
