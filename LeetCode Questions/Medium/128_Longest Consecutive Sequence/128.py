# submitted at May 25, 2024 15:02
class Solution:
  def longestConsecutive(self, nums: list[int]) -> int:
    numSet = set(nums)
    max_length = 0

    for i in nums:
      # 確認是否為連續數字的開頭
      if i-1 not in numSet:
        # 是的話一直確認他的下一個值是否有在陣列中   
        long = 0
        while (i+long) in numSet:
          long += 1
        # 當下一個值沒有在陣列中時，與max_length比較取最大
        # 因為有可能一個陣列有很多組連續數字
        # 而搞不好第一組連續數字就是最大，不做紀錄的話就會被後面較小的給蓋過
        max_length = max(max_length, long)
    return max_length