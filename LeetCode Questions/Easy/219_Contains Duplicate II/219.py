# submitted at Apr 30, 2024 11:43
class Solution:
  def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
    hashTable = {}
    for i, value in enumerate(nums):
      if value in hashTable and abs(i - hashTable[value]) <= k:
        # 如果有重複的值，且當前位置與先前紀錄在hashTable的位置相差 <= k
        return True
      # 將陣列的值當作key, 當前陣列位置當作value, 寫進hashTable
      hashTable[value] = i
    # 並未找到有相同的值
    return False