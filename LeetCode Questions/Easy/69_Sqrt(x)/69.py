# submitted at Apr 22, 2024 21:24
class Solution:
  def mySqrt(self, x: int) -> int:
    a_point = 0
    b_point = x
    
    while a_point <= b_point:
      half = (a_point+b_point) // 2
      
      if half ** 2 == x:
        return half
      
      if half ** 2 < x:
        a_point = half + 1
      else:
        b_point = half - 1
    return b_point