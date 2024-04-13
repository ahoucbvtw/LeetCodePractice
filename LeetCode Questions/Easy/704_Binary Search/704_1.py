# submitted at Apr 11, 2024
class Solution:
  def search(self, nums: list[int], target: int) -> int:
    i = 0
    k = len(nums) - 1

    # 2分搜尋法
    while True:
      search_index = (i+k) // 2
      if 0 <= search_index < len(nums) and i != k:
        # search_index不會超過或小於原先的陣列長度
        if nums[search_index] > target:
          k = search_index - 1
        elif nums[search_index] == target:
          break
        else:
          i = search_index + 1
      else:
        # i,k 2個頭尾指標若指到同一個位置時表示找到答案了，或找不到任何值
        if i == k and nums[search_index] == target:
          # 若i,k 指標相同且nums[search_index] == target表示找到
          break
        else:
          # 找不到
          search_index = -1
          break

    return search_index