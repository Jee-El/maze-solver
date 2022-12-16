import pygame


class GUI:
    def __init__(self, maze, maze_solver, algorithm_name):
        pygame.display.set_caption("Maze Solver by Jee El")

        self.maze = maze
        self.maze_solver = maze_solver
        self.is_gbfs = algorithm_name == "gbfs"
        self.__set_algorithm(algorithm_name)

        self.square_size = 50
        self.set_squares_margins()
        self._screen = pygame.display.set_mode(
            [self.maze.width * self.square_size, self.maze.height * self.square_size]
        )
        self.char_to_color = {
            "#": "black",
            " ": "white",
            "X": "dodgerblue1",
            "O": "chartreuse3",
            "A": "red",
            "B": "green",
        }
        self._running = True
        self.escape_is_pressed = False

    def launch(self):
        pygame.init()
        self._font = pygame.font.SysFont("Arial", 25)
        clock = pygame.time.Clock()
        self.draw_maze()
        pygame.display.flip()

        solved = False
        while self._running:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._running = False

            if not solved:
                solved_path = self.solve(self)
                solved = True
                self.draw_path(solved_path, True)
                pygame.display.flip()
        pygame.quit()

    def set_squares_margins(self):
        self.squares_margins = {}
        top_margin = 0
        for i in range(self.maze.height):
            left_margin = 0
            for j in range(self.maze.width):
                self.squares_margins[(i, j)] = (left_margin, top_margin)
                left_margin += self.square_size
            top_margin += self.square_size

    def draw_maze(self):
        for i in range(self.maze.height):
            for j in range(self.maze.width):
                char = self.maze.rows[i][j]
                self.draw_square(
                    *self.squares_margins[(i, j)], self.char_to_color[char]
                )
                if self.is_gbfs:
                    manhattan_distance = self.maze_solver.get_manhattan_distance(
                        (i, j), self.maze.end
                    )
                    self.draw_manhattan_distance(
                        *self.squares_margins[(i, j)], manhattan_distance
                    )

    def draw_path(self, path, solved=False):
        for i, j in path:
            self.draw_square(
                *self.squares_margins[(i, j)],
                self.char_to_color["O" if solved else "X"]
            )
            if self.is_gbfs:
                manhattan_distance = self.maze_solver.get_manhattan_distance(
                    (i, j), self.maze.end
                )
                self.draw_manhattan_distance(
                    *self.squares_margins[(i, j)], manhattan_distance
                )

    def draw_square(self, left_margin, top_margin, color):
        square = pygame.Rect(
            left_margin, top_margin, self.square_size, self.square_size
        )
        pygame.draw.rect(self._screen, color, square)

    def draw_manhattan_distance(self, left_margin, top_margin, manhattan_distance):
        text = self._font.render(str(manhattan_distance), True, "black")
        left_margin += (self.square_size - text.get_width()) / 2
        top_margin += (self.square_size - text.get_height()) / 2
        self._screen.blit(text, (left_margin, top_margin))

    def __set_algorithm(self, algorithm_name):
        algorithms = {
            "dfs": self.maze_solver.solve_with_dfs,
            "bfs": self.maze_solver.solve_with_bfs,
            "gbfs": self.maze_solver.solve_with_gbfs,
        }
        self.solve = algorithms[algorithm_name]

    def pause(self):
        if self.escape_is_pressed:
            return
        next = False
        while not next:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    next = event.key in [pygame.K_RETURN, pygame.K_ESCAPE]
                    self.escape_is_pressed = event.key == pygame.K_ESCAPE
