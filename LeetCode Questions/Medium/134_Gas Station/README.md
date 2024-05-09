# LeetCode 134 Gas Station
There are `n` gas stations along a circular route, where the amount of gas at the `ith` station is `gas[i]`.

You have a car with an unlimited gas tank and it costs `cost[i]` of gas to travel from the `ith` station to its `next (i + 1)th` station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays `gas` and `cost`, return *the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return `-1`*. If there exists a solution, it is **guaranteed** to be **unique**

Example 1:
```
Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3
Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.
```

Example 2:
```
Input: gas = [2,3,4], cost = [3,4,3]
Output: -1
Explanation:
You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 0. Your tank = 4 - 3 + 2 = 3
Travel to station 1. Your tank = 3 - 3 + 3 = 3
You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
Therefore, you can't travel around the circuit once no matter where you start.
```

Constraints:

- `n == gas.length == cost.length`
- `1 <= n <= 10^5`
- `0 <= gas[i], cost[i] <= 10^4`

## Topic
- Array
- Greedy

## My Thinking
首先必須要先將 `每間加油站的加油量總和`，以及 `到達每間加油站的距離總和` 做比較<br>若一開始題目給的 `每間加油站的加油量總和` < `到達每間加油站的距離總和`，那不管從哪裡開始出發是絕對無法繞行一圈。

接著就是按照題目所說一間一間加油站去做比對，若發現此加油站加的油量無法到達下一間時，表示不能從這間開始，因此換下一間開始計算。

### Complexity
Time complexity: O(n)
> 因為使用 `for迴圈` 進行遍歷計算 `加油量與加油站間距離的差`，因此為**O(n)**

Space complexity: O(1)
> 在解題上從頭到尾都只有使用 `gas[i]` 或 `cost[i]` 直接獲取指定加油站的加油量以及到達下一間的距離，因此為**O(1)**
