# submitted at May 14, 2024 23:54
class Solution:
  def maxArea(self, height: list[int]) -> int:
    maxWaterContainer = 0
    L_point = 0
    R_point = len(height) - 1
    
    while L_point < R_point:
      # 計算可裝水的面積
      x_axis = R_point - L_point
      minHight = min(height[R_point], height[L_point])
      aera = minHight * x_axis
      
      if aera > maxWaterContainer:
        # 若此次計算的面積 > 之前面積 => 紀錄
        maxWaterContainer = aera
      
      if height[R_point] >= height[L_point]:
        L_point += 1
      elif height[R_point] < height[L_point]:
        R_point -= 1
    return maxWaterContainer