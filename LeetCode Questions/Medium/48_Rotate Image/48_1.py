# submitted at May 21, 2024 22:55
class Solution:
  def rotate(self, matrix: list[list[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    rows = len(matrix)
    # 將矩陣變成轉置矩陣
    for y in range(rows):
      for x in range(y):
        matrix[x][y], matrix[y][x] = matrix[y][x], matrix[x][y]

    # 將轉置矩陣每一行從中間對半鏡向對調
    for y in range(rows):
      # 每一行都要進行鏡像對調
      # 利用 L, R 向中間靠攏，直到L<R停止
      # 在這停止會剛好有2種結果
      # 1. row = 奇數，中間那一排不會對調(L=R)
      # 2. row = 偶數，沒有中間那排全部對調
      L, R = 0, rows-1
      while L < R:
        matrix[y][L], matrix[y][R] = matrix[y][R], matrix[y][L]
        L += 1
        R -= 1