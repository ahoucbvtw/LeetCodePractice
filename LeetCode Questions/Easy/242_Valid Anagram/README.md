# LeetCode 242 Valid Anagram
Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
```
Input: s = "anagram", t = "nagaram"
Output: true
```

Example 2:
```
Input: s = "rat", t = "car"
Output: false
```

Constraints:

- `1 <= s.length, t.length <= 5 * 10^4`
- `s` and `t` consist of lowercase English letters.

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?


## Topic
- Hash Table
- String
- Sorting

## My Thinking
因為要找出字串 `t` 是否為字串 `s` 所組成，因此製作字串 `s` 的字母/符號 `Hash Table`，最後再利用此 `Hash Table` 與字串 `t` 比對，若都有在 `Hash Table` = True，只要有一個沒有 = False

### Complexity
Time complexity: O(mn)
> 因為題目並為說明兩者字串長度相同，再加上使用2個 `for迴圈` 去遍歷 `t` 和 `s`，因此為 **O(mn)**<br>但若題目有說兩者字串相同的話，則會變成 **O(n)**

Space complexity: O(mn)
> 理由同上，使用 `for迴圈` 去遍歷 `t` 和 `s` 字串再加上兩者陣列並不一定相同長度，因此為 **O(mn)**