# submitted at May 26, 2024 02:44
class Solution:
  def merge(self, intervals: list[list[int]]) -> list[list[int]]:
    intervals.sort()
    output = []
    start, end = intervals[0][0], intervals[0][1]

    if len(intervals) == 1:
      return intervals

    for i in range(1, len(intervals)):
      left, right = intervals[i]
      if (start <= left <= end) and (right >= end):
        # 不需要探討新區間左邊是否會小於前區間
        # 因為已經先排列完畢，因此新區間的左邊一定會 >= 前區間左邊
        # 所以只需要確認新區間的左邊是否在前區間內(包含相等)以及新區間右邊是否>=前區間右邊
        end = right
      if end < left:
        # 新區間左邊 > 前區間右邊，表示新區間並沒有與前區間重疊
        # 換下一個區間前先將更改完畢的區間加入陣列
        output.append([start, end])
        # 將start, end更換成新區間去比較接下來的區間
        start, end = left, right
      # 由於寫法問題，若到最後都沒有經歷換下一個區間或最後剛好換下一個區間
      # 都會漏掉，因此要添加
      if i == len(intervals) - 1:
        output.append([start, end])
    return output