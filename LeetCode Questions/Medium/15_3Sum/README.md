# LeetCode 15 3Sum
Given an integer array nums, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

Notice that the solution set must not contain duplicate triplets.

Example 1:
```
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
```

Example 2:
```
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
```

Example 3:
```
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
```

Constraints:

- `3 <= nums.length <= 3000`
- `-10^5 <= nums[i] <= 10^5`

Hint 1
```
So, we essentially need to find three numbers x, y, and z such that they add up to the given value. 

If we fix one of the numbers say x, we are left with the two-sum problem at hand!
```

Hint 2
```
For the two-sum problem, if we fix one of the numbers, say x, we have to scan the entire array to find the next number y, which is value - x where value is the input parameter. 

Can we change our array somehow so that this search becomes faster?
```

Hint 3
```
The second train of thought for two-sum is, without changing the array, can we use additional space somehow? 

Like maybe a hash map to speed up the search?
```
## Topic
- Array
- Sorting
- Two Pointers

## My Thinking
題目說需要在陣列中找到 `3個值相加 = 0`，因此可以當作 `x + y + z = 0`。

透過題目的 `Hint1` 以及 `NeetCode的影片` 說明，讓我知道了如何簡化 `x + y + z = 0` 的算法。

此方法就是 `先固定x`，再去使用 `Two Pointers` 計算其他2個值相加是否等於 `-x` => `-x = y + z`。

因此就以此為方針開始解題步驟：
- 先將陣列進行排列，在 `Python` 中使用 `sort()`，此時 Time complexity = $O(nlog_n)$
  - 至於為什麼要先進行排序的原因是，陣列中可能會有重複值。<br>因此當先前x值已經被計算過，又再次遇到相同x值則不需要再次計算，因為題目要求不能有相同的數字排列。<br><br>ex: `[-3, 4, -1], [-1, -3, 4]` 此兩個陣列排列是相同的因此只會取其中一個。
- 先使用 `for迴圈` 固定x值，然後再用 `while迴圈` 搭配 `Two Pointers` 找出符合題目要求 `-x = y + z`。<br>計算 `y 和 z` 時若遇到符合條件時除了將數值新增外，也還需要繼續遍歷下去。<br>因為**題目沒有說一個陣列3個值相加 = 0 的解只會有一個**。
  - 注意：**因為找到符合條件的點後還需要繼續搜尋是否有下一個。**<br>此時也可以再次固定其中一個，另一個進行移動。<br>不過移動的那一方也需要進行是否有重複值的考慮，遇到相同值則繼續向前或向後一步直到除了 `固定的x` 以後的陣列值全部遍歷完畢。

ps1. 
```
在固定x值的時候，若當 固定的值已經 > 0 時，則無須繼續進行計算。

因為陣列已經進行升序排列，後續的值不管與此x相加都不可能 = 0。
```

ps2. 
```
若 -x ≠ y + z 時左右指標的移動方式：

1. 當 -x < y + z -> 右指標向中間靠近一步。
2. 當 -x > y + z -> 左指標向中間靠近一步。
```

> 詳細解說影片: **By NeetCode**
> 
> [![3Sum - Leetcode 15 - Python](https://img.youtube.com/vi/jzZsG8n2R9A/hqdefault.jpg)](https://www.youtube.com/watch?v=jzZsG8n2R9A)


### Complexity
Time complexity: $O(n^2)$
> 因為首先使用 `Python` 的 `sort()`，此時為 $O(nlog_n)$。<br><br>接著為了找出題目要求 `x + y + z = 0`，採用固定x值再遍歷其餘陣列值而使用了 `2個迴圈`，而此作法為 $O(n^2)$。<br><br>所以總共為 $O(nlog_n) + O(n^2)$，但 `Time complexity` 永遠取最壞的結果，因此為 **$O(n^2)$**

Space complexity: O(1)
> 由於進行相加的值都是直接從 `陣列中指定位置取得`，因此為**O(1)**