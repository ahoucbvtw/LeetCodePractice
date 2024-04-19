# submitted at Apr 19, 2024 20:45
class Solution:
  def containsDuplicate(self, nums: list[int]) -> bool:
    table = {}
    for i in nums:
      if i not in table:
        table[i] = 1
      else:
        return True
    return False