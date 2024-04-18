# LeetCode 28 Find the Index of the First Occurrence in a String
Given two strings `needle` and `haystack`, return the index of the first occurrence of `needle` in `haystack`, or `-1` if `needle` is not part of `haystack`.

Example 1:

```
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
```

Example 2:

```
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
```

Constraints:

- `1 <= haystack.length, needle.length <= 10^4`
- `haystack` and `needle` consist of only lowercase English characters.

## Topic
- Two Pointers
- String
- String Matching

## My Thinking
此題目要找`needle`的字串是否有出現在`haystack`中，如果有則輸出在`haystack`的開頭的位置，沒有則`-1`

因此我的解題思路：
1. 使用迴圈去遍歷`haystack`字串，但是一次遍歷`needle`字串的長度<br>ex: haystack = "leetcode", needle = "leeto", 第一次搜尋`leetc != needle`, 第二次搜尋`eetco != needle`...
2. 找到就直接輸出`needle`在`haystack`開頭位置，沒有則輸出`-1`