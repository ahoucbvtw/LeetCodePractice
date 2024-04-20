# submitted at Apr 20, 2024 00:18
class Solution:
  def rotate(self, nums: list[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    if k > len(nums):
      k = k % len(nums)
    nums.reverse()
    nums[:k] = reversed(nums[:k])
    nums[k:] = reversed(nums[k:])