# LeetCode 128 Longest Consecutive Sequence
Given an unsorted array of integers `nums`, return *the length of the longest consecutive elements sequence.*

You must write an algorithm that runs in `O(n)` time.

Example 1:
```
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
```

Example 2:
```
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
```

Constraints:

- `0 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

## Topic
- Array
- Union Find
- Hash Table

## My Thinking
由於此題目有特別要求 `Time complexity = O(n)`，也因為此要求，無法使用 `排序sort`。<br>因為 `排序sort` 的 `Time complexity = O(nlogn)`。

因為題目的限制(`非排序陣列` 和 `不能使用排序`)，在判斷連續數字的起點位置時會顯的些許麻煩，不過可以使用 `Set` 和 `HashTable`。<br>藉由使用這2個方法，在搜尋陣列中的值時 `Time complexity = O(1)`。<br>在此次採用 `Set` 的寫法，也是 `NeetCode` 的寫法。

另外要如何判斷該數值為連續數字的起點？<br>只需要搜尋有沒有數值比該值還小的數值存在，若不存在則該值即為一個連續數字的起點。

解題思路：
- 先將題目 `Input nums` 給 `Set`，方便後續查詢數值使用。
- 遍歷陣列判斷數值是否為連續數字的起點。
  - 是：<br>繼續一直檢查 `該值+1` 是否有在 `Set` 中直到找不到為止。<br>最後統計此連續數值的長度，若有比先前出現的還要長則覆蓋。
  - 否：<br>不會進行計算，因為該值並非起點，計算長度時會不準。

> 參考影片: **By NeetCode**
>
> `Time complexity = O(n), Space complexity = O(n)`
> 
> [![Leetcode 128 - LONGEST CONSECUTIVE SEQUENCE](https://img.youtube.com/vi/P6RZZMu_maU/hqdefault.jpg)](https://www.youtube.com/watch?v=P6RZZMu_maU)


### Complexity
Time complexity: O(n)
> 因為需要遍歷陣列中所有數字，而非使用排序，因此為 **O(n)**

Space complexity: O(n)
> 因為使用在確認數值是否有在陣列中前有先將陣列轉變成 `Set`，並額外儲存成一個變數空間中，因此為 **O(n)**。