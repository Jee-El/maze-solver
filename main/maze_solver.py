import pygame
from queue import PriorityQueue


class MazeSolver:
    def __init__(self, maze, adjacency_list):
        self.maze = maze
        self.adjacency_list = adjacency_list
        self.dfs_explored_states = 0
        self.bfs_explored_states = 0
        self.gbfs_explored_states = 0

    def solve_with_dfs(self, gui):
        start = self.maze.start
        end = self.maze.end
        solution = self.__dfs(gui, start, end, [(start, [start])], {start})
        return solution or self.__no_solution_found()

    def solve_with_bfs(self, gui):
        start = self.maze.start
        end = self.maze.end
        solution = self.__bfs(gui, start, end)
        return solution or self.__no_solution_found()

    def solve_with_gbfs(self, gui):
        start = self.maze.start
        end = self.maze.end
        solution = self.__gbfs(gui, start, end)
        return solution or self.__no_solution_found()

    def __dfs(self, gui, start, end, queue, visited_vertices):
        vertex, path = queue.pop(0)
        self.dfs_explored_states += 1

        while self.__enter_is_not_pressed():
            pass
        gui.draw_path(path)
        pygame.display.flip()

        if vertex == end:
            print("Explored states : ", self.dfs_explored_states)
            return path

        for adjacent_vertex in self.adjacency_list[vertex]:
            if adjacent_vertex not in visited_vertices:
                visited_vertices.add(adjacent_vertex)
                new_path = path + [adjacent_vertex]
                new_queue = queue + [(adjacent_vertex, new_path)]
                solved_path = self.__dfs(gui, start, end, new_queue, visited_vertices)

                if solved_path:
                    return solved_path

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
                print("Explored states : ", self.bfs_explored_states)
                return path

            for adjacent_vertex in self.adjacency_list[vertex]:
                if adjacent_vertex not in visited_vertices:
                    visited_vertices.add(adjacent_vertex)
                    new_path = path + [adjacent_vertex]
                    queue.append((adjacent_vertex, new_path))

    def __gbfs(self, gui, start, end):
        priority_queue = PriorityQueue()
        manhattan_distance = self.get_manhattan_distance(start, end)
        priority_queue.put((manhattan_distance, start, [start]))
        visited_vertices = {start}

        while not priority_queue.empty():
            _, vertex, path = priority_queue.get()
            self.gbfs_explored_states += 1

            while self.__enter_is_not_pressed():
                pass
            gui.draw_path(path)
            pygame.display.flip()

            if vertex == end:
                print("Explored states : ", self.gbfs_explored_states)
                return path

            for adjacent_vertex in self.adjacency_list[vertex]:
                if adjacent_vertex not in visited_vertices:
                    visited_vertices.add(adjacent_vertex)
                    new_path = path + [adjacent_vertex]
                    manhattan_distance = self.get_manhattan_distance(
                        adjacent_vertex, end
                    )
                    priority_queue.put((manhattan_distance, adjacent_vertex, new_path))

    def get_manhattan_distance(self, start, end):
        return abs(start[0] - end[0]) + abs(start[1] - end[1])

    def __enter_is_not_pressed(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return False
        return True

    def __no_solution_found(self):
        raise Exception("No Solution was found")
