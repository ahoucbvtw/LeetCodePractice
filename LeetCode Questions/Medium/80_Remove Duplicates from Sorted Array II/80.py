# submitted at May 05, 2024 21:42
class Solution:
  def removeDuplicates(self, nums: list[int]) -> int:
    slow_point = 0
    sameCount = 1
    for fast_point in range(1, len(nums)):
      # 統計相同數值個數
      if nums[slow_point] == nums[fast_point]:
        sameCount += 1
      else: 
        # 當發現不相同數值時，將此統計改成新的值
        # 因為包含自己，所以初始值=1
        sameCount = 1
      # 若相同數量統計<=2, 慢指針+1;慢指針下一個值=快指針當前值
      if sameCount <= 2:
        nums[slow_point+1] = nums[fast_point]
        slow_point += 1
    # 慢指針當前位置+1 = 按照題目要求排序好的陣列尾端
    # 至於慢指針當前位置+2以後數值則不予理會
    return slow_point + 1