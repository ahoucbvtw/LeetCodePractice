# submitted at Apr 14, 2024 12:14
class Solution:
  def countNegatives(self, grid: list[list[int]]) -> int:
    # 因為題目說不管grid(m,n)內的m或n的排列均屬於遞減
    # 因此可以確定的是每個n的數量肯定都一樣，否則m列無法形成遞減
    neg_amount = 0
    n_length = len(grid[0])
    
    for m in range(len(grid)):
      n = 0
      while n < n_length:
        if grid[m][n] < 0:
          neg_amount += 1
        n += 1
    return neg_amount