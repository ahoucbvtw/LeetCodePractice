# LeetCode 228 Summary Ranges

You are given a **sorted unique** integer array `nums`.

A **range** `[a,b]` is the set of all integers from `a` to `b` (inclusive).

Return the *smallest sorted* list of ranges *that cover all the numbers in the array exactly*. That is, each element of `nums` is covered by exactly one of the ranges, and there is no integer `x` such that `x` is in one of the ranges but not in `nums`.

Each range `[a,b]` in the list should be output as:

- `"a->b"` if `a != b`
- `"a" if` if `a == b`

Example 1:

```
Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
```

Example 2:

```
Input: grid = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"
```

Constraints:

- `0 <= nums.length <= 20`
- `-231 <= nums[i] <= 231 - 1`
- **All the values of `nums` are unique**.
- `nums` **is sorted in ascending order**.

## Topic
- Array

## My Thinking

建立2個a,b=0指標，a只用來定位區間的最小值，b會隨著迴圈內慢慢+1
因為是已經陣列排好且區間內一定是連號(後一個數 - 前一個數 = 1)
因此
1. 使用`nums[i] - nums[b_point] > 1`判斷是否連號
2. 最後再判斷i是最後一個數字的時候情況