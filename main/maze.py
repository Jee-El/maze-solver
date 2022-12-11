class Maze:
    def __init__(self, maze_file):
        self.to_str = maze_file.read()
        maze_file.close()

        self.__to_list()
        self.__to_bool_list()

        self.start, self.end = self.start_and_end()

        self.height = len(self.list)
        self.width = len(self.list[0])

    def start_and_end(self):
        start, end = None, None
        for i in range(len(self.list)):
            if not start and "A" in self.list[i]:
                start = (i, self.list[i].index("A"))
            if not end and "B" in self.list[i]:
                end = (i, self.list[i].index("B"))
            if start and end:
                return (start, end)
        self.__no_start_or_no_end()

    def __to_bool_list(self):
        self.bool_list = [
            [char in [" ", "A", "B"] for char in row] for row in self.list
        ]

    def __to_list(self):
        maze_list = self.to_str.split("\n")
        self.list = [[*line.upper()] for line in maze_list]

    def __no_start_or_no_end(self):
        error_msg = """
      A starting point and/or an ending point were/was not found.
      Make sure to mark them, respectively, with A and B in your maze text file.
    """
        raise Exception(error_msg)
