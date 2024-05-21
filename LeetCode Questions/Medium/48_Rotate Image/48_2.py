# submitted at May 21, 2024 23:27
class Solution:
  def rotate(self, matrix: list[list[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    L, R = 0, len(matrix) - 1

    while L < R:
      # 因為順時針轉90度，原先(0,0)->(0,最後一個)
      # 因此不需要在判斷最後一個值
      # 所以總共要對調 R-L 次
      for i in range(R-L):
        T, B = L, R
        # 使用額外空間旋轉前儲存第一個值，讓該空格可以先被覆蓋
        temp = matrix[T][L+i]
        
        # 因為左上已經先把值額外儲存，所以用逆時針方式將值一直覆蓋
        # 將左下移動到左上
        matrix[T][L+i] = matrix[B-i][L]
        
        # 將右下移動到左下
        matrix[B-i][L] = matrix[B][R-i]
        
        # 將右上移動到右下
        matrix[B][R-i] = matrix[T+i][R]
        
        # 將額外空間儲存值移動到右上
        matrix[T+i][R] = temp
      L += 1
      R -= 1