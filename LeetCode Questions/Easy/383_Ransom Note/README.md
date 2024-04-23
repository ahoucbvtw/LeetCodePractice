# LeetCode 383 Ransom Note
Given two strings `ransomNote` and `magazine`, return `true` *if `ransomNote` can be constructed by using the letters from `magazine` and `false` otherwise*.

Each letter in `magazine` can only be used once in `ransomNote`.

Example 1:
```
Input: ransomNote = "a", magazine = "b"
Output: false
```

Example 2:
```
Input: ransomNote = "aa", magazine = "ab"
Output: false
```

Example 3:
```
Input: ransomNote = "aa", magazine = "aab"
Output: true
```

Constraints:

- `1 <= ransomNote.lengmagazineth, magazine.length <= 10^5`
- `ransomNote` and `magazine` consist of lowercase English letters.


## Topic
- Hash Table
- String
- Counting

## My Thinking
因為 `magazine` 是要與 `ransomNote` 做比較<br>因此利用 `magazine` 去製作 `Hash Table`，最後再用 `ransomNote` 與 `Hash Table` 比對

只要 `ransomNote` 有的字母，而 `magazine` 沒有，表示不需要繼續比較直接 => `False`<br>相反，若 `ransomNote` 全部跑完都與 `magazine` => `True`

### Complexity
Time complexity: O(mn)
> 因為使用2個不同長度的 `for迴圈` 去遍歷以及製作 `hashtable` 和 `ransomNote`，因此為 **O(mn)**

Space complexity: O(n)
> 雖然在與 `Hash Table` 比對的時候使用 `hashTable[i]` 判斷是否不在裡面是 **O(1)**
> 但是在這之前因為使用 `for迴圈` 去製作 `Hash Table` ，因此為 **O(n)**