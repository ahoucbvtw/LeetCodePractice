# LeetCode 20 Valid Parentheses
Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Example 1:
```
Input: s = "()"
Output: true
```

Example 2:
```
Input: s = "()[]{}"
Output: true
```

Example 3:
```
Input: s = "(]"
Output: false
```

Constraints:

- `1 <= s.length <= 10^4`
- `s` consists of parentheses only `'()[]{}'`.

## Topic
- Stack
- String

## My Thinking
由於題目要確認 `Input` 的值內當出現 `(`, `[`, `{` 時一定要在字串後面某個地方出現相對應的 `)`, `]`, `}` 將這些括弧關起來。

因此若字串中若出現 `)`, `]`, `}` 先，而 `(`, `[`, `{` 在後面，視為 `打開 = False`。<br>ex: `]}{[` -> 就算都有出現對應的括弧，這樣會使括弧打開並未關起來。

因此解題思路為：
- 利用 `Stack` 資料結構的特性，為每一個 `()`, `[]`, `{}` 做判斷，也就是每次此 `Stack` 陣列中都只會有 `(`, `[`, `{` 開頭做相對應的括弧判斷。
- 利用迴圈遍歷，當 `Stack` 陣列為空，第一個遇到 `)`, `]`, `}` 時，直接 `return False`，因為不管如何此括弧都不會被關閉。
- 每當 `Stack` 陣列中 `(`, `[`, `{` 在一下次遍歷有遇到對應的括弧，就可以把該值從 `Stack` 陣列中剔除。<br>最後若陣列還有未關閉的括弧則 `return False`。


### Complexity
Time complexity: O(n)
> 因為是使用迴圈遍歷查詢字串，因此為 **O(n)**

Space complexity: O(n)
> 因為在迴圈遍歷確認是否出現的括弧可以被關閉而使用 `Stack` 陣列去紀錄，因此為 **O(n)**。