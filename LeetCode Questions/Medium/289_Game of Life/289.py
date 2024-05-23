# submitted at May 23, 2024 23:04
class Solution:
  def gameOfLife(self, board: list[list[int]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    # 1: 如果附近有2-3 => 1, 否則0
    # 0: 如果附近有3 => 1, 否則0
    
    # 原本  改變成  state
    #  0     0      0
    #  1     0      1
    #  0     1      2
    #  1     1      3
    
    # 1 -> 0 state=1, 0 -> 1 state=2是有原因的
    # 因為若是 0 -> 1 state=1, 1 -> 0 state=2的話
    # 在計算周圍8個鄰居時會因為該點的上方已經改成狀態而下方未改
    # 但state=1 原先值=0 又會與 下方未改成狀態的1搞混
    rows, cols = len(board), len(board[0])
    
    def neighbors(y, x):
      counts = 0  # 紀錄8方位鄰居有幾個1
      for i in range(y-1, y+2):
        for j in range(x-1, x+2):
          # 要判斷矩陣(上下左右四邊不能超出範圍)以及(不需要判斷自己本身那一格)
          if i < 0 or j < 0 or i == rows or j == cols or (i == y and j == x):
            continue
          # 因為計算周圍鄰居時，該點的上面及左邊都是更改完狀態
          # 因此要多計算更改完狀態前為存活1的值
          if board[i][j] in [1, 3]:
            counts += 1
      return counts
    
    for y in range(rows):
      for x in range(cols):
        counts = neighbors(y, x)
        # 判斷該格子要轉變成哪個狀態
        if board[y][x] == 1:
          # 原先是1
          if counts in [2, 3]:
            board[y][x] = 3
        else:
          # 原先是0
          if counts == 3:
            board[y][x] = 2
    # 將狀態變更成更改後的值(更改後的存活1或死亡0)
    for y in range(rows):
      for x in range(cols):
        match board[y][x]:
          case 2 | 3:
            board[y][x] = 1
          case 1:
            board[y][x] = 0