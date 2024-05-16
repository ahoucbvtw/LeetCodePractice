# LeetCode 209 Minimum Size Subarray Sum
Given an array of positive integers `nums` and a positive integer `target`, return *the **minimal length** of a subarray whose sum is greater than or equal to* `target`. If there is no such subarray, return `0` instead.

Example 1:
```
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
```

Example 2:
```
Input: target = 4, nums = [1,4,4]
Output: 1
```

Example 3:
```
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
```

Constraints:

- `1 <= target <= 10^9`
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^4`

**Follow up**: If you have figured out the `O(n)` solution, try coding another solution of which the time complexity is `O(n log(n))`.

## Topic
- Array
- Prefix Sum
- Binary Search
- Sliding Window

## My Thinking
由於此題並未說清楚他要的 `subarray` 是要從原陣列中取出且由左往右連續在一起的，而不能有跳號的情形。<br>ex: nums = [2,3,1,2,4,3], subarray = [1,2,4], [3,1]; subarray ≠ [2,3,4], [3,4]。

因此在解題時，不能先將 `nums` 進行排序。

此題一樣使用 `Two Pointers` 不過是變種，因為要計算 `subarray` 的總和，因此也可以看做一個 `window`，而在演算法中此解法為 `Sliding Window`。<br>顧名思義就是利用左右兩個指標而匡起來的區間來進行運算。

有了區間的概念後，就比較好解題。

題目要求：
1. `subarray` 區間內總和 >= target
2. 求最小 `subarray` 區間

解題思路如下：
- 先將ans設置成最大值，方便後續進行最小 `subarray` 區間比較
- `L, R` 都設置在 `index = 0`，每當 `L, R` 所包圍的區間內總和 < target 時，將 `R + 1` 藉此獲得額外的數值看看是否 `總和能符合題目第一要求`。
- 當 `題目第一要求` 符合時，就需要判斷 `題目第二要求`，計算此區間的長度是否與先前區間長度還要短，短的話則寫入。
  - 另外由於題目陣列都是正整數，因此不需要再次將R往右移動繼續計算<br>因為以舊L為開頭的區間已經找到最小長度，繼續往右邊移動一樣達成 `題目第一要求` 但不達成 `題目第二要求`。
  - 此時便需要將 `L+1` 為開頭，R則繼續與上一次相同<br>(因為若R往回變成 `新L+1` 是沒意義，此區間的值同樣在先前 `舊L` 區間一定 < target)<br>ex: target = 6, nums = [1,2,2,4,5]<br>`舊L區間` = [1,2,2,4] => 若 `新L區間` = `L+1, R=新L+1` = [2,2] 總和 < target

> 詳細解說影片: **By NeetCode**
> 
> [![Minimum Size Subarray Sum - Leetcode 209 - Python](https://img.youtube.com/vi/aYqYMIqZx5s/hqdefault.jpg)](https://www.youtube.com/watch?v=aYqYMIqZx5s)


### Complexity
Time complexity: O(n)
> 雖然有使用 `2個迴圈`，但其實此 `while迴圈` 就只是單純用來判斷是否 >= target<br>有的話只需要繼續將 `L+1` 找尋最小的區間即可，因此為 **O(n)**

Space complexity: O(1)
> 由於進行總和相加時 `陣列中指定位置取得`，因此為**O(1)**