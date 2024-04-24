# LeetCode 202 Happy Number
Write an algorithm to determine if a number `n` is happy.

A **happy number** is a number defined by the following process:

- Starting with any positive integer, replace the number by the sum of the squares of its digits.
- Repeat the process until the number equals 1 (where it will stay), or it **loops endlessly in a cycle** which does not include 1.
- Those numbers for which this process **ends in 1 are happy**.

Example 1:
```
Input: n = 19
Output: true
Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
```

Example 2:
```
Input: n = 2
Output: false
```

Constraints:

- `1 <= n <= 231 - 1`

## Topic
- Hash Table
- Math
- Two Pointers

## My Thinking
建立一 `0 ~ 9 的平方表` **(可有可無)** 以及建立 `repeatTable` 用來記錄計算 Happy number 時是否重複循環 **(需要)** <br>每進行一次計算都寫進去，直到 = 1，則輸出 `True`<br>若出現重複值 `(已經存進repeatTable)`，則輸出 `False`

### Complexity
Time complexity: O(n)
> 因為每次計算時非個位數的話就需要使用 `for迴圈` 去遍歷其個別數字的平方和，因此為 **O(n)**

Space complexity: O(n)
> 因為使用 `for迴圈` 去製作可能重複的 `Hash Table` ，因此為 **O(n)**