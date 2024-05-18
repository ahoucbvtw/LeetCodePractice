# LeetCode 3 Longest Substring Without Repeating Characters

Given a string `s`, find the length of the **longest substring** without repeating characters.

Example 1:
```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
```

Example 2:
```
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```

Example 3:
```
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
```

Constraints:

- `0 <= s.length <= 5 * 10^4`
- `s` consists of English letters, digits, symbols and spaces.

## Topic
- String
- Hash Table
- Sliding Window

## My Thinking
此題解題思路與 [209 Minimum Size Subarray Sum](https://github.com/ahoucbvtw/LeetCodePractice/tree/main/LeetCode%20Questions/Medium/209_Minimum%20Size%20Subarray%20Sum) 相同，並且雖然沒有明說，但其要求的 `substring` 也一定是不能有跳號的情況必須要連續的。

利用 `Two Pointers` 的2個左右指標找尋所圍成的最大區域 `window` 且此範圍內不能有重複值出現。

因此解題思路如下：
- 設定 `Set` 用來存放目前檢視的區域內是否出現重複值。
  - 當然使用 `Array` 或 `Queue` 也可以實現。<br>但此兩種資料格式在 `判斷某個值是否在這之中` 時 `Time complexit = O(n)`，在此題目寫法較不合適，一邊遍歷一邊判斷就可能會造成 `Time complexit = O(n^2)`。<br>另外我自己也有試過，若使用 `Queue` 時間上確實比 `Set` 慢。
  - `HashTable` 此資料格式也可以使用，並且題目也在此歸類上，但我並不會使用。<br>雖然在 `判斷某個值是否在這之中` 時 `Time complexit = O(1)`，但是在要進行刪除時，會變得稍嫌麻煩，步驟有點多。
- 先將 `L固定在 index = 0`，而 `R會一直慢慢向右遍歷`。<br>在遍歷的期間每遍歷一次就 `會把R對應的值放入Set內` 並且 `比較新的R值是否有出現在Set內`。<br>若新的R值有在裡面此時就會進入 `while迴圈流程`，將 `原先區域的左邊L + 1` 並 `刪除Set內的該值`，直到新區域內不會出現有重複值為止。
  - ex: s = "pwwkew", 當R=2時會發現此時區域內有重複值 => `(p,w,w)`。<br>此時就會進入while迴圈流程，`將L+1 => 新區域 (w,w)`。<br>但很明顯新區域還是有重複值，不符合題目要求，`因此再次將L+1 => (w)`。<br>此時L和R都在同一位置上，且新區域並沒有重複值，因此跳脫 `while迴圈流程` 繼續找尋區域內未重複的最大區域。

### Complexity
Time complexity: O(n)
> 雖然有使用 `2個迴圈`，但其實此 `while迴圈` 也只是用來判斷區域內是否有重複值<br>當有重複值則 `L+1` 直到並未有重複值為止才繼續以新L為起點，R繼續向右找尋最大的區間，因此可以變相地說此 `while迴圈` 是加快排除不合適的選項，因此為 **O(n)**

Space complexity: O(1)
> 由於不管是在判斷是否在Set內或是Set的增刪都是 `取得字串中指定位置值`，因此為 **O(1)**