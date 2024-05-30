# submitted at May 28, 2024 23:22
class Solution:
  def findMinArrowShots(self, points: list[list[int]]) -> int:
    points.sort()
    ans = len(points)
    prev = points[0]
    
    for i in range(1, len(points)):
      if points[i][0] <= prev[1]:
        # 如果重疊，將先前區間改成取此兩區間重疊位置
        # 因為我們射出去的箭必須剛好是多顆氣球重疊處，才能以最少之箭打爆所有氣球
        # 每找到一次重疊就扣除最壞的len(points)箭矢解
        # 並且ans - 1
        # [1,4] [2,6] => [2,4]
        # [1,5] [2,4] => [2,4]
        prev = [points[i][0], min(prev[1], points[i][1])]
        ans -= 1
      else:
        prev = points[i]
    return ans