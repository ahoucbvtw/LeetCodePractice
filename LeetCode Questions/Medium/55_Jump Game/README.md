# LeetCode 55 Jump Game
You are given an integer array `nums`. You are initially positioned at the array's **first index**, and each element in the array represents your maximum jump length at that position.

Return `true` *if you can reach the last index, or `false` otherwise.*

Example 1:
```
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
```

Example 2:
```
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
```

Constraints:

- `1 <= nums.length <= 10^4`
- `0 <= nums[i] <= 10^5`

## Topic
- Array
- Dynamic Programming
- Greedy

## My Thinking
此題說起點位在 `陣列起始位置 index=0`，並且每次可以移動該位置值的最大值<br>ex: array[0] = 5, 此時可以往前`1-5步`都可以

要判斷此陣列若從 `陣列起始位置 index=0` 出發的話是否可以到達`陣列最後的位置 index=len(array)-1`

若是按照DP的算法，可以畫成一棵樹，並且可以透過已經走過確認無法到達的點不繼續走<br>但 `Time complexity` 會造成 `O(n^2)`，並且浪費很多 `Memory` 去紀錄重複無法到達的點位，效能較為不佳

因此此時使用 `Greedy演算法`，此演算法是一種**在每一步選擇中都採取在當前狀態下最好或最佳解**。<br>也就是此題可以從終點開始往前看，檢查每一個點的數值是否可以到達終點<br>可以 => 將新的終點設置成剛才判斷的點直到整個陣列遍歷完畢

ps.為什麼可以這樣做？<br>因為已經確定此點可以到達題目的終點，所以接下來只要繼續判斷前面的點是否可以到達此新設置的終點即可，直到最後迴圈遍歷結束(符合 `Greedy演算法` 的定義，**在每一步選擇中都採取在當前狀態下最好或最佳解**)

> 詳細解說影片: **By NeetCode**
> 
> [![Jump Game - Greedy - Leetcode 55](https://i.ytimg.com/vi/Yan0cv2cLy8/hqdefault.jpg?sqp=-oaymwEcCPYBEIoBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLCv84Z_tQkCPagG1asSQl_MBlxMnQ)](https://www.youtube.com/watch?v=Yan0cv2cLy8)

### Complexity
Time complexity: O(n)
> 因為使用 `Greedy演算法` 一步一步進行計算 `(for迴圈)` 是否可以到達終點，因此為**O(n)**

Space complexity: O(1)
> 此題只有使用 `nums[i]` 直接指定獲取陣列值，因此為**O(1)**