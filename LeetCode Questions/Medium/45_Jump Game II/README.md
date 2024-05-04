# LeetCode 45 Jump Game II
You are given a **0-indexed** array of integers `nums` of length `n`. You are initially positioned at `nums[0]`.

Each element `nums[i]` represents the maximum length of a forward jump from index `i`. In other words, if you are at `nums[i]`, you can jump to any `nums[i + j]` where:

- `0 <= j <= nums[i]`
- `i + j < n`

Example 1:
```
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
```

Example 2:
```
Input: nums = [2,3,0,1,4]
Output: 2
```

Constraints:

- `1 <= nums.length <= 10^4`
- `0 <= nums[i] <= 1000`
- **It's guaranteed that you can reach** `nums[n - 1]`.

## Topic
- Array
- Dynamic Programming
- Greedy

## My Thinking
此題目與 [**<font color=#FF0000></b>LeetCode 55 Jump Game</font>**](https://github.com/ahoucbvtw/LeetCodePractice/tree/main/LeetCode%20Questions/Medium/55_Jump%20Game) 相同，差別在於這題是要尋找最少步數到達 `nums[n - 1]`，而非探討是否可以到達 `nums[n - 1]`。

此題第一時間想到的解法就是 `Dynamic Programming`，利用將確認過無法到達 `nums[n - 1]` 的index路線給存入額外記憶體空間達成減少計算量時間，因為若不這樣操作此 `Time complexity` 會是 **<font color=#FF0000></b>O($n^2$)</font>** 執行效率會非常低。

不過換個思路，使用 `Greedy` 特性搜尋當下位置最佳的解，但並非如 [**<font color=#FF0000></b>LeetCode 55 Jump Game</font>**](https://github.com/ahoucbvtw/LeetCodePractice/tree/main/LeetCode%20Questions/Medium/55_Jump%20Game) 使用方式相同，需要換個使用方式。

假設現在有一陣列 `nums = [2,6,1,3,5,1,3,0,1,4,0,3]`，初始條件與題目給的相同 `起始位置index=0` 且 `此陣列必定可以到達 nums[n - 1]`。<br>設置一區間，此區間有左右邊界，初始時左右邊界都為0，也就是 `初始區間 = [2]`。<br>經過 `nums[0] = 2` 的計算，最遠可以到達 `index = 0+2`，最近可以到達 `index = 0+1`。<br>因此可以確定在 `nums[0] = 2` 當下若往前走第一次時必定或落在 `區間[6,1]` 的範圍。<br>同樣操作計算新區間 `[6,1]` 內的數字各別能到達的區間範圍 = `[3,5,1,3,0]`，因此若在第一區間任一位置時往前再走一次時必定會在此新第二區間範圍。<br>依此類推，透過藉由計算到底需要花多少區間(不包含初始區間，因為那是第0步)，即可得知此陣列需要花最少步數到達 `nums[n - 1]`。


> 詳細解說影片: **By NeetCode**
> 
> [![Jump Game II - Greedy - Leetcode 45](https://i.ytimg.com/vi/dJ7sWiOoK7g/hqdefault.jpg?sqp=-oaymwEcCNACELwBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLDcX31Sly6WL8ezfNADGDG7zLYtnA)](https://www.youtube.com/watch?v=dJ7sWiOoK7g&t=640s)


### Complexity
Time complexity: O(n)
> 因為使用 `Greedy` 一步一步進行區間內最大步數計算，是否可以到達終點，因此為**O(n)**

Space complexity: O(1)
> 此題只有使用 `nums[i]` 直接指定獲取陣列值，因此為**O(1)**