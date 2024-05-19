# submitted at May 19, 2024 17:13
import collections

class Solution:
  def isValidSudoku(self, board: list[list[str]]) -> bool:
    row = collections.defaultdict(set)
    col = collections.defaultdict(set)
    subbox = collections.defaultdict(set)

    for x in range(9):
      for y in range(9):
        if board[x][y] == ".":
          # 不需判斷空格
          continue
        if (board[x][y] in row[x]) or (board[x][y] in col[y]) or (board[x][y] in subbox[x//3, y//3]):
          return False
        row[x].add(board[x][y])
        col[y].add(board[x][y])
        subbox[x//3, y//3].add(board[x][y])
    return True