# LeetCode 290 Word Pattern
Given a `pattern` and a string `s`, find if `s` follows the same `pattern`.

Here follow means a full match, such that there is a bijection between a letter in `pattern` and a non-empty word in `s`.

Example 1:
```
Input: pattern = "abba", s = "dog cat cat dog"
Output: true
```

Example 2:
```
Input: pattern = "abba", s = "dog cat cat fish"
Output: false
```

Example 3:
```
Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
```

Constraints:

- `1 <= pattern.length <= 300`
- `pattern` contains only lower-case English letters.
- `1 <= s.length <= 3000`
- `s` contains only lowercase English letters and spaces `' '`.
- `s` does not contain any leading or trailing spaces.
- All the words in `s` are separated by a single space.

## Topic
- Hash Table
- String

## My Thinking
製作一陣列是利用find找出 `pattern` 重複出現的字母的第一次出現位置<br>而因為s字串中間有空格，因此利用split改成陣列去判斷相同單詞是在陣列的第一次出現位置<br>最後將2者陣列做比較，相同true，不相同false

### Complexity
Time complexity: O(n)
> 因為要找出字串 `s` 是否與 `pattern` 以相同的規律進行排列，因此若將字串 `s` split，肯定與 `pattern` 的第一次出現字母陣列數量一樣<br>且因為使用 `for迴圈` 去遍歷 `s` 和 `pattern` 的字串製作陣列再加上兩者陣列相同長度，因此為 **O(n)**

Space complexity: O(n)
> 理由同上，使用 `for迴圈` 去遍歷 `s` 和 `pattern` 的字串製作陣列再加上兩者陣列相同長度，因此為 **O(n)**