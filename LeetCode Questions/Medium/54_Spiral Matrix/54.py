# submitted at May 20, 2024 22:31
class Solution:
  def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
    ans = []
    L, R = 0, len(matrix[0])
    T, B = 0, len(matrix)
    
    # 要一直順時鐘繞直到把所有值給找完
    while (L < R) and (T < B):
        # 從最左上開始順時鐘繞一圈可拆分成4個步驟
        # 1. 上面：左 -> 右
        for i in range(L, R):
          ans.append(matrix[T][i])
        T += 1

        # 2. 右邊：上 -> 下
        for i in range(T, B):
          ans.append(matrix[i][R-1])
        R -= 1

        # 在這邊要檢查確保是否matrix為 '1 x n' or 'n x 1'
        if (L >= R) or (T >= B):
          break
        
        # 3. 下面：右 -> 左
        for i in range(R-1, L-1, -1):
          ans.append(matrix[B-1][i])
        B -= 1

        # 4. 左邊：下 -> 上
        for i in range(B-1, T-1, -1):
          ans.append(matrix[i][L])
        L += 1
    return ans