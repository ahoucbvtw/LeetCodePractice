# submitted at Apr 14, 2024 11:52
class Solution:
  def negbinary(self, array: list[int]) -> int:
    leftP = 0
    rightP = len(array)
    # 用左指標找尋最大負整數位置
    # 也就是最後左指摽最後的位置會是該陣列最大負整數的位置
    # 所以若要計算個數時只需要用該陣列的長度 - 左指標 = 負整數數量
    while leftP < rightP:
      mid = leftP + (rightP - leftP) // 2
      if array[mid] < 0:
        rightP = mid
      else:
        leftP = mid + 1
    return len(array) - leftP

  def countNegatives(self, grid: list[list[int]]) -> int:
    neg_count = 0

    for m_array in grid:
      neg_count += self.negbinary(m_array)
    
    return neg_count