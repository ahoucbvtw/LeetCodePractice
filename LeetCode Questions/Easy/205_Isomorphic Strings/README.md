# LeetCode 205 Isomorphic Strings
Given two strings `s` and `t`, determine if they are isomorphic.

Two strings s and `t` are isomorphic if the characters in `s` can be replaced to get `t`.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

Example 1:
```
Input: s = "egg", t = "add"
Output: true
```

Example 2:
```
Input: s = "foo", t = "bar"
Output: false
```

Example 3:
```
Input: s = "paper", t = "title"
Output: true
```

Constraints:

- `1 <= s.length <= 5 * 10^4`
- `t.length == s.length`
- `s` and `t` consist of any valid ascii character.


## Topic
- Hash Table
- String

## My Thinking
利用 `for迴圈` 搜尋2個字串其重複字母的位置，並兩者做比較<br>相同 = `True`，不相同 = `False`

### Complexity
Time complexity: O(n)
> 因為使用 `for迴圈` 去遍歷 `s` 和 `t` 的字串搜尋各別相同字母的位置排序是否一樣，且題目也說 `s` 和 `t` 的字串長度相同，因此為 **O(n)**

Space complexity: O(n)
> 因為使用 `for迴圈` 去搜尋各別相同字母位置排序是否一樣，且題目也說 `s` 和 `t` 的字串長度相同，因此為 **O(n)**