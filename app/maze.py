class Maze:
    def __init__(self, maze_file):
        self.to_str = maze_file.read()
        maze_file.close()

        self.__to_rows()
        self.__to_bool_rows()

        self.start, self.end = self.__start_and_end()

        self.height = len(self.rows)
        self.width = len(self.rows[0])

    def __start_and_end(self):
        start, end = None, None
        for i in range(len(self.rows)):
            if not start and "A" in self.rows[i]:
                start = (i, self.rows[i].index("A"))
            if not end and "B" in self.rows[i]:
                end = (i, self.rows[i].index("B"))
            if start and end:
                return (start, end)
        self.__no_start_or_no_end()

    def __to_bool_rows(self):
        self.bool_rows = [
            [char in [" ", "A", "B"] for char in row] for row in self.rows
        ]

    def __to_rows(self):
        maze_list = self.to_str.split("\n")
        self.rows = [[*line.upper()] for line in maze_list]

    def __no_start_or_no_end(self):
        error_msg = """
      A starting point and/or an ending point were/was not found.
      Make sure to mark them, respectively, with A and B in your maze text file.
    """
        raise Exception(error_msg)
