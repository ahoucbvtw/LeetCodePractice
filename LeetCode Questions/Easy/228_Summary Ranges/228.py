class Solution:
  def summaryRanges(self, nums: list[int]) -> list[str]:
    a_point = 0
    b_point = 0
    output = []
    
    if len(nums) == 1:
      return [f"{nums[0]}"]

    for i in range(1, len(nums)):
      # print('i = ', i)
      # print(f'a_point = {a_point}, b_point = {b_point}')
      # b_point會永遠+1=i，也就是一直兩兩相鄰比對
      if nums[i] - nums[b_point] > 1:
        if a_point == b_point:
            # a_point == b_point 表示第一次遍歷時nums[0]和nums[1]就有跳號
            output.append(f'{nums[a_point]}')
        else:
            # 若nums[i] - nums[b_point]一直沒有>1表示這之前一直都是+1的連號
            # 當相差>0時表示nums[a_point]->nums[b_point]都是+1連號
            output.append(f'{nums[a_point]}->{nums[b_point]}')
        # 只要有寫入output，就需要把 a_point 往前移動至i的位置
        a_point = i
      
      # 判斷目前i的位置是否為陣列的最後一個
      if i == len(nums) -1:
        if nums[a_point] == nums[i]:
            # 若此時nums[i] - nums[b_point] > 1，表示最後一個值不屬於上一個區間的值
            # 則在上一個for迴圈內會先新增前一個區間nums[a_point]->nums[b_point]
            # 且因為a_point被往前移動至i的位置(陣列的最後一個)，最後再加入它至output
            output.append(f'{nums[i]}')
        else:
            # 若a_point沒有因為nums[i] - nums[b_point] > 1
            # 表示此最後一個值是最後一個區間的尾
            output.append(f'{nums[a_point]}->{nums[i]}')
      b_point += 1
    return output