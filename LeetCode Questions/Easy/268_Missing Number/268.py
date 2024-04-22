# submitted at Apr 22, 2024 22:40
class Solution:
  def missingNumber(self, nums: list[int]) -> int:
    hashTable = {}

    for i in nums:
      hashTable[i] = 1

    for i in range(len(nums)+1):
      try:
        hashTable[i]
      except:
        return i
    return None