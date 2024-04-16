# LeetCode 58 Length of Last Word
Given a string `s` consisting of words and spaces, return *the length of the **last** word in the string*.

A **word** is a maximal substring consisting of non-space characters only.

Example 1:

```
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
```

Example 2:

```
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
```

Example 3:

```
Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
```

Constraints:

- `1 <= s.length <= 10^4`
- `s` consists of only English letters and spaces `' '`.
- There will be at least one word in `s`.

## Topic
- String

## My Thinking

題目已經確保`字串s`一定會`有一個英文單字`，且空格一定是 `' '` 組成

而此題要找`字串s`中最後一個英文單字的字數，因此首先
1. 避免`字串s`頭尾有空格，先去除頭尾的空格
2. 使用 `split(' ')` 把每一個英文單字給區分開
3. 計算最後一個英文單字的長度