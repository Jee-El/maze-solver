class Maze:
  def __init__(self, maze_file):
    self.hashtag_str = maze_file.read()

    self.hashtag_arr = self.to_hashtag_arr(maze_file)

    maze_file.close()

    self.start, self.end = self.start_and_end(self.hashtag_arr)

    self.bool_list = self.to_bool_list(self.hashtag_arr)

    self.height = len(self.hashtag_arr)
    self.width = len(self.hashtag_arr[0])

  def to_bool_list(self, maze_rows):
    return [
        [True if char in [' ', 'A', 'B'] else False for char in row] for row in maze_rows
    ]

  def to_hashtag_arr(self, maze_file):
    maze_file.seek(0)
    return [
        list(row.replace('\n', '')) for row in maze_file.readlines()
    ]

  def start_and_end(self, maze):
    start, end = None, None
    for i in range(len(maze)):
      if not start and 'A' in maze[i]:
        start = (i, maze[i].index('A'))
      if not end and 'B' in maze[i]:
        end = (i, maze[i].index('B'))
      if start and end:
        return (start, end)
