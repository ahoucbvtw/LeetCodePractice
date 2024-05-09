# submitted at May 09, 2024 00:11
class Solution:
  def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
    carTank = 0
    startStation = 0
    if sum(gas) < sum(cost):
      # 若總油量 < 總消耗 => 不管從哪出發都不可能巡迴一圈，一定會停在半路
      return -1
    
    for i in range(len(gas)):
      carTank += (gas[i] - cost[i])
      if carTank < 0:
        # 表示若從此加油站出發的話
        # 汽車油箱油量不夠到下一個車站
        carTank = 0
        startStation = i + 1
    # 若總油量 > 總消耗，但是又找不到可以巡迴一圈的加油站 return -1
    return -1 if startStation == len(gas) else startStation