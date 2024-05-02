# submitted at May 01, 2024 14:57
class Solution:
  def removeDuplicates(self, nums: list[int]) -> int:
    a_index = 0  # slow point

    for b_index in range(1, len(nums)):
      # 當fast/slow point比較相同時，只需要將fast point進行+1
      # 等fast/slow point不相同時，再將slow point+1替換成fast point值
      # 並且slow point也要往前，因為已經不需要比對此數值，換比對新的重複值
      if nums[a_index] != nums[b_index]:
        nums[a_index+1] = nums[b_index]
        a_index += 1
    # 因為a_index是slow point
    # 因此最後a_index的位置即是已經排序好且刪除重複值的陣列最後一個位置
    # a_index後面的值則是重複值不需要理，所以return共有a_index + 1已刪除重複的值
    return a_index + 1 