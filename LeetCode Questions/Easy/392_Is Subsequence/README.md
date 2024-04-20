# LeetCode 392 Is Subsequence
Given two strings `s` and `t`, return `true` if `s` is a *subsequence* of `t`, or `false` otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., `"ace"` is a subsequence of `"abcde"` while `"aec"` is not).

Example 1:
```
Input: s = "abc", t = "ahbgdc"
Output: true
```

Example 2:
```
Input: s = "axc", t = "ahbgdc"
Output: false
```

Constraints:

- `0 <= s.length <= 100`
- `0 <= t.length <= 10^4`
- `s` and `t` consist only of lowercase English letters.

Follow up: Suppose there are lots of incoming `s`, say `s1, s2, ..., sk` where `k >= 10^9`, and you want to check one by one to see if `t` has its subsequence. In this scenario, how would you change your code?

## Topic
- Two Pointers
- String
- Dynamic Programming

## My Thinking
題目已經很清楚給出範例，只要 `s字串有按照順序從左至右出現在t字串` 中，即s字串是t字串的子字串
```
ex: s="abc", 如果是子字串的話則t="??a????b?c??" (?為隨機小寫字母)

如果t="c???a??b?"，雖然t字串中有包含s字串中的3個字母
但因為並非按照順序 "abc" 出現，因此s並非t的子字串
```

<br><br>解題思路很單純，使用 `Two Pointers`

設置2個指標，一個指標是遍歷s字串用，另一個是遍歷t字串用

當遍歷s字串用的 `指標剛好到達s字串的最後一個字母時 = s是t的子字串`

反之若 `遍歷t字串的指標已經跑完，遍歷s字串尚未結束 = s不是t的子字串`

### Complexity
Time complexity: O(n)
> 使用迴圈遍歷整個 `t` 字串，所以是 **O(n)**

Space complexity: O(1)
> 每一次進行字串比對時都是直接指定字串位置 `t[i] == s[a_point]`，所以是 **O(1)**