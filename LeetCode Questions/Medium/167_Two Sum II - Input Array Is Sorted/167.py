# submitted at May 13, 2024 22:49
# O(n)
class Solution:
  def twoSum(self, numbers: list[int], target: int) -> list[int]:
    firstP = 0
    sencodP = len(numbers) - 1
    
    for i in range(len(numbers)):
      total = numbers[firstP] + numbers[sencodP]
      match total:
        case total if total == target:
          return [firstP+1, sencodP+1]
        case total if total < target:
          # 如果總和 < target，firstP 指標向前一步
          firstP += 1
        case total if total > target:
          # 如果總和 > target，sencodP 指標向後一步
          sencodP -= 1