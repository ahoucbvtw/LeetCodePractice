# submitted at May 16, 2024 23:41
class Solution:
  def minSubArrayLen(self, target: int, nums: list[int]) -> int:
    ans = len(nums)  # 一開始先將ans設置成最大值，方便後續進行比較
    total = 0
    L = 0
    
    if sum(nums) < target:
      # 因為第一次是直接採用最大區間計算
      # 如果連最大區間計算都還是 < target
      # 則表示此陣列所有值不管怎麼加都不會 >= target
      return 0

    for R in range(len(nums)):
      # 若區間陣列總和 < target，表示此區間陣列總和不夠
      # 所以將區間最右邊位置向右拓張直到剛好找到總和 >= target區間
      total += nums[R]
      while total >= target:
        # 若區間陣列總和 >= target 時
        # 表示以L為開頭的區間已經找到最小總和 >= target 的 subarray
        # 因此不需要再次將R往右移動繼續計算
        # 因為題目說陣列都是正整數
        # 所以已經找到最小的subarray若右邊再次往右移動一格時一樣 >= target
        # 但是總長度已經不是最小的，所以此時只需要將L往前移動一格
        # 換計算以新L為開端，R則繼續與上一次相同(因為若R往回變成新L+1是沒意義，此區間同樣在先前舊L的區間，且一定 < target)
        # 當然若此新L的區間總和若 < target，就會跳脫此迴圈繼續將R向右拓張
        # 相反若新L的區間總和 >= target，就會繼續將L+1直到總和 < target
        ans = min((R-L)+1, ans)
        
        # 因為要計算新L+1區間總和，所以要先將原先區間總和減去原先L的值
        total -= nums[L]
        L += 1
    return ans