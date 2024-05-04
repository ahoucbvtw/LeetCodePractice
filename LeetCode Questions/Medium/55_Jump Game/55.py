# submitted at May 03, 2024 09:30
class Solution:
  def canJump(self, nums: list[int]) -> bool:
    last_index = len(nums) - 1
    for i in range(len(nums)-1, -1, -1):
      if i + nums[i] >= last_index and i != len(nums) - 1:
      # 使用Greedy演算法，計算當下的值是否有最好或最佳的解抵達終點
      # 當下index+當下數值若可以超過或剛好到達最後index
      # 則可以試作當下的位置是絕對可以到達最後index(不管走幾步直到當下值的最大步數)
      # 因此即可把最後index向前移動至當前index繼續往前判斷前面是否可以到達此新的最後index
      # 因為若前面點能到達此新最後index，且新最後index也可以到達原始陣列的最後index，
      # 即表示前面的點必定能到達最後index
        last_index = i
    return True if last_index == 0 else False