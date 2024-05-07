# submitted at May 07, 2024 15:31
# Time O(n), Space O(n)
class Solution:
  def productExceptSelf(self, nums: list[int]) -> list[int]:
    ans = list()
    
    # 紀錄每個當前值的左邊與右邊的乘機 
    # 因為 i = 0 時左邊沒有值，因此給定值1
    # 同樣 i = -1 時右邊沒有值，因此給定值1
    left, right = len(nums) * [1], len(nums) * [1]
    
    # 製作每個當前值的左邊所有值的乘機(計算左邊時直接跳過i=0)
    for i in range(1, len(nums)):
      left[i] = nums[i-1] * left[i-1]
    
    # 製作每個當前值的右邊所有值的乘積(計算右邊時直接跳過i=-1)
    for i in range(len(nums)-2, -1, -1):
      right[i] = nums[i+1] * right[i+1]
    
    # 將每個當前值的左邊與右邊按照順序相乘
    for i in range(len(nums)):
      ans.append(left[i] * right[i])
    
    return ans