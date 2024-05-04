# submitted at May 04, 2024 12:35
class Solution:
  def jump(self, nums: list[int]) -> int:
    ans = 0
    goal_index = len(nums) - 1
    # 當下區間點位能到達下一個區間的左右index
    # ex: nums = [2,6,1,3,5,1,3,0,1,4,0,3]
    # 第一次區間[2], 則他可以到達下一個區間範圍=[6,1]
    # 當下區間[6,1], 則下一個可到達的區間範圍=[3,5,1,3,0]依此類推
    # 將Greedy用區間方式來計算會需要執行多少次
    nextAera_R, nextAera_L = 0, 0
    while nextAera_R < goal_index:
      can_move_farthest = 0
      for i in range(nextAera_L, nextAera_R+1):
      # 不管該區域有多少值，都會計算該區域內值走最大步數後會在的index
        can_move_farthest = max(can_move_farthest, i + nums[i])
      nextAera_L = nextAera_R + 1
      nextAera_R = can_move_farthest    
      ans += 1
    return ans