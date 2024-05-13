# LeetCode 167 Two Sum II - Input Array Is Sorted
Given a **1-indexed** array of integers `numbers` that is already ***sorted in non-decreasing order***, find two numbers such that they add up to a specific `target` number. Let these two numbers be `numbers[index1]` and `numbers[index2]` where `1 <= index1 < index2 <= numbers.length`.

Return *the indices of the two numbers*, `index1` and `index2`, added by one as an integer array `[index1, index2]` of length 2.

The tests are generated such that there is **exactly one solution**. You **may not** use the same element twice.

Your solution must use only constant extra space.

## Topic
- Array
- Two Pointers
- Binary Search

## My Thinking
這裏使用 `Two Pointers` 設置2個指標，一個在陣列的頭部，一個在陣列的尾部。

經由每次計算 `2個指標所在的值總和判斷是否 = target`。<br>`若 < target: 頭部的指標向前+1` ; `若 > target: 尾部的指標向後-1`。<br>直到 `總和 = target` 為止。

### Complexity
Time complexity: O(n)
> 因為使用陣列去一個一個遍歷 `哪2個數值相加 = target`，因此為**O(n)**

Space complexity: O(1)
> 都只有使用 `numbers[firstP]` 或 `numbers[sencodP]` 查詢指定值，並且此兩個數值總和也是指定值的相加，因此為**O(1)**