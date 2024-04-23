# LeetCode 268 Missing Number
Given an array `nums` containing `n` distinct numbers in the range `[0, n]`, return *the only number in the range that is missing from the array*.

Example 1:
```
Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3].
2 is the missing number in the range since it does not appear in nums.
```

Example 2:
```
Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2].
2 is the missing number in the range since it does not appear in nums.
```

Example 3:
```
Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9].
8 is the missing number in the range since it does not appear in nums.
```

Constraints:

- `n == nums.length`
- `1 <= n <= 10^4`
- `0 <= nums[i] <= n`
- All the numbers of `nums` are **unique**.

Follow up: Could you implement a solution using only `O(1)` extra space complexity and `O(n)` runtime complexity?

## Topic
- Array
- Hash Table
- Math
- Binary Search
- Bit Manipulation
- Sorting

## My Thinking
題目給定 `nums`，並且要找出 `[0, n]` 間 `nums` 缺少的數字，其中 `n = len(nums)`

按照題目的 Follow up 要求<br>`Time complexity = O(n)`, `Space complexity = O(1)`

因此使用 `hashTable` 去紀錄目前 `nums` 有什麼數字<br>再使用 `for迴圈` 遍歷 `[0, n]` 間的數字並且比對是否有在 `hashTable` 內

### Complexity
Time complexity: O(n)
> 因為使用 `for迴圈` 去遍歷 `nums` 和 `[0, n]` 間的數字，因此為 **O(n)**

Space complexity: O(n)
> 雖然在與 `Hash Table` 比對的時候使用 `hashTable[i]` 判斷是否不在裡面是 **O(1)**
>
> 但是在這之前因為使用 `for迴圈` 去製作 `Hash Table` ，因此為 **O(n)**