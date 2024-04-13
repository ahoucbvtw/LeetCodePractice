# submitted at Apr 12, 2024 17:28
class Solution:
  def maximumCount(self, nums: list[int]) -> int:
    # O(n)
    pos_counts = 0
    neg_counts = 0

    for num in nums:
      if num < 0:
        neg_counts += 1
      elif num > 0:
        pos_counts += 1
    return max(pos_counts, neg_counts)