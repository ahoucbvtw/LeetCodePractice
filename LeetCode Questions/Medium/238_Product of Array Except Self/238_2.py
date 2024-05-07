# submitted at May 07, 2024 15:32
# Time O(n), Space O(1)
class Solution:
  def productExceptSelf(self, nums: list[int]) -> list[int]:
    ans = len(nums) * [1]

    # 先製作每個當前值的左邊所有值的乘機(計算左邊時直接跳過i=0)
    for i in range(1, len(nums)):
      ans[i] = ans[i-1] * nums[i-1]

    # 製作每個當前值的右邊所有值的乘機(right)，i=-1時因為右邊沒有值，因此給1定值
    # 並直接與每個當前值得左邊進行相乘即可得到解
    right = 1
    for i in range(len(nums)-1, -1, -1):
      ans[i] = ans[i] * right
      right = right * nums[i]
    
    return ans