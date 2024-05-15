# submitted at May 15, 2024 23:58
class Solution:
  def threeSum(self, nums: list[int]) -> list[list[int]]:
    output = []
    nums.sort()
    # x+y+z=0 => -x = y+z
    # 先定x值，剩下2個值拆分成R,L兩點計算
    for i, num in enumerate(nums): 
      # x值
      if num > 0:
        # 因為已經排序好了
        # 若x=大於0的值，則右邊值勢必也>0
        # 所以就算相加也不會符合題目要求
        # 因此不需要計算
        break
      if i > 0 and num == nums[i - 1]:
        # 因為已經排序，所以一樣值會再一起
        # 而一樣的x值不需要重複再計算
        # 但是要確保一定要計算第一次，也就是x = nums[0]的值
        continue
        
      # 取得y,z值，並且符合題目要求 => -x = y+z
      L, R = i + 1, len(nums) - 1
      while L < R:
        twoSum = nums[L] + nums[R]
        if -num < twoSum:
          R -= 1
        elif -num > twoSum:
          L += 1
        else:
          output.append([num, nums[L], nums[R]])
          L += 1  # L或R向中間靠近都可以，不管是哪種都可以全部都跑一次
          # 如果下一次Ｌ值還是一樣，跳過不用再計算
          while (L < R) and (nums[L] == nums[L - 1]):
            L += 1
    return output