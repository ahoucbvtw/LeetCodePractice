# LeetCode 219 Contains Duplicate II

Given an integer array `nums` and an integer `k`, return `true` *if there are two distinct indices `i` and `j` in the array* such that `nums[i] == nums[j]` and `abs(i - j) <= k`.

Example 1:
```
Input: nums = [1,2,3,1], k = 3
Output: true
```

Example 2:
```
Input: nums = [1,0,1,1], k = 1
Output: true
```

Example 3:
```
Input: nums = [1,2,3,1,2,3], k = 2
Output: false
```

Constraints:

- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`
- `0 <= k <= 10^5`

## Topic
- Array
- Hash Table
- Sliding Window

## My Thinking
使用 `for迴圈` 從頭開始遍歷，並將該值當作 `Hash Table` 的 Key ; index 當作 Value。<br>當繼續遍歷下去搜尋是否有相同值，有相同值時就會確定此條件是否達成 `當下的 index - 先前紀錄的 index <= k`，未達成則將相同值的新index覆寫，繼續比對

### Complexity
Time complexity: O(n)
> 因為使用 `for迴圈` 方法從頭開始遍歷，因此為 **O(n)**

Space complexity: O(n)
> 雖然在比對是否相同的時候是直接使用key/value，但是因為此 `Hash Table` 是使用 `for迴圈` 製作，因此為 **O(n)**