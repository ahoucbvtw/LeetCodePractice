# LeetCode 1351 Count Negative Numbers in a Sorted Matrix

Given a `m x n` matrix `grid` which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in `grid`.

Example 1:

```
Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.
```

Example 2:

```
Input: grid = [[3,2],[1,0]]
Output: 0
```

Constraints:
- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 100`
- `-100 <= grid[i][j] <= 100`

**Follow up**: Could you find an `O(n + m)` solution?

## Topic
- Array
- Binary Search
- Matrix

## My Thinking

- 使用題目所說的 `O(n + m)` 時間複雜度撰寫 => `1351_1.py`
- 因為題目說明此 `grid` 矩陣內所有的陣列都是排列好，因此可以使用二分搜尋法 => `1351_2.py`