# submitted at May 27, 2024 23:14
class Solution:
  def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
    # 有4種情況
    # 1情況：新加入的區間最大值 < intervals內所有區間
    ## 直接在最左邊加入該區間
    # 2情況：新加入區間最小值 > intervals內所有區間
    ## 直接在最右邊加入該區間
    # 3情況：新加入區間在intervals內某兩區間的中間並未重疊
    ## 雖然說是在中間，但是新加入的區間也是 < 目前遍歷的區間，因此適用第1種情況
    # 4情況：新加入區間在intervals內某n個區間重疊
    ## 先計算第一個重疊，再看下一個是否有重疊
    ## 有在進行合併，沒有就將此合併新增至output
    output = []

    if len(intervals) == 0:
      return [newInterval]
    
    for i in range(len(intervals)):
      ### 1 ###
      if newInterval[1] < intervals[i][0]:
        output.append(newInterval)
        return output + intervals[i:]
      ### 2 ###
      elif newInterval[0] > intervals[i][1]:
        output.append(intervals[i])
      ### 4 ###
      else:
        # 每個區間一個一個慢慢比較，看是否沒有重疊
        # 有重疊就找兩者的最小值和最大值當作新區間範圍
        newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
    # 最後全部區間遍歷完再加入newInterval的原因是因為
    # 2,4這2種情況
    # 因為2會是新區間 > 所有原陣列區間，而因為撰寫方式緣故需要在最後加入newInterval
    # 4則是因為不確定是否新加入區間是否有橫跨多個舊區間，一般在中間部分橫跨沒問題，但若是剛好有橫跨在舊區間的最後時就會少加
    output.append(newInterval)
    
    return output