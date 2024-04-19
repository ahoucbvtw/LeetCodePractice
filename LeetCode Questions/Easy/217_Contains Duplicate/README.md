# LeetCode 217 Contains Duplicate
Given an integer array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct.

Example 1:
```
Input: nums = [1,2,3,1]
Output: true
```

Example 2:
```
Input: nums = [1,2,3,4]
Output: false
```

Example 3:
```
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
```

Constraints:

- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

## Topic
- Array
- Hash Table
- Sorting

## My Thinking
題目要找陣列中 `至少出現2次 (>=2)`，若有則輸出 `True`，否則輸出 `False`

我使用 `hash table` 去紀錄出現的值，若沒出現則紀錄

假如相同的值已經出現(`i in table`)，則直接跳脫迴圈不必全部找完輸出 `True`

若陣列中的值全部遍歷完畢都沒發現 `至少出現2次 (>=2)` 的值則輸出 `False`

### Complexity
Time complexity: O(n)
> 因為是從頭開始針對陣列進行遍歷，所以是 **O(n)**

Space complexity: O(1)
> 每一次比對都是針對 `hash table` 中的特定值去比對是否存在 `if i not in table`，所以是 **O(1)**