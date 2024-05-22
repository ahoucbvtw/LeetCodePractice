# submitted at May 22, 2024 22:58
class Solution:
  def setZeroes(self, matrix: list[list[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    cols = len(matrix[0])
    rows = len(matrix)
    
    row0_temp = [False] * rows
    col0_temp = [False] * cols
    
    # 找出哪一行、哪一列有0並記錄
    for y in range(rows):
        for x in range(cols):
            if (matrix[y][x] == 0):
                row0_temp[x], col0_temp[y] = True, True
    
    # 按照額外空間紀錄的哪一行、哪一列有0進行原矩陣填0
    for y in range(rows):
        for x in range(cols):
            # 當紀錄的該行或該列任一=True以及該座標矩陣不為0時填0
            # 因為原先已經是0的就不需要再次填入0
            if ((col0_temp[y] == True) or (row0_temp[x] == True)) and matrix[y][x] != 0:
                matrix[y][x] = 0