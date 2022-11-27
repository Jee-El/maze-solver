class Maze:
  def __init__(self, maze_file, start, end):
    self.start = start
    self.end = end

    self.hashtag_str = maze_file.read()

    maze_file.seek(0)

    self.hashtag_arr = self.hashtag_arr(maze_file)

    maze_file.close()

    self.to_bool = self.to_bool(self.hashtag_arr)

    self.height = len(self.hashtag_arr)
    self.width = len(self.hashtag_arr[0])

  def to_bool(self, maze_rows):
    return [
        [True if char in [' ', 'A', 'B'] else False for char in row] for row in maze_rows
    ]

  def hashtag_arr(self, maze_file):
    return [
        list(row.replace('\n', '')) for row in maze_file.readlines()
    ]
