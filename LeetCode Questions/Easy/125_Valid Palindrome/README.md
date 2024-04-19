# LeetCode 125 Valid Palindrome
A phrase is a **palindrome** if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `true` if it is a palindrome, or `false` otherwise.

Example 1:

```
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
```

Example 2:

```
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
```

Example 3:

```
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
```

Constraints:

- `1 <= s.length <= 2 * 10^5`
- `s` consists only of printable ASCII characters.

## Topic
- Two Pointers
- String

## My Thinking
`palindrome` 定義為正讀和反讀都是相同的句子(前後對稱)<br><br>ex: `abccba`, `a`, ` `

題目要求尋找給定的字串中是否為 `英數字(Alphanumeric)` 的 `palindrome`，按照定義因此需要建立2個指標<br><br>**一個指標是從頭開始遍歷字串，另一個指標是從尾部開始遍歷字串**

<br>當2個指標位置中有不一樣，表示此`字串 ≠ palindrome`，相反則 `字串 = palindrome`

### Complexity
Time complexity: O(n)
> 使用 `Two Pointers` 進行頭尾比對時是使用for迴圈一個一個對新 `s1` 字串進行比對

Space complexity: O(n)
> 因為我在 `125.py` 建立 `s1` 來儲存只有`英數字的字串`，並且是使用for迴圈一個一個檢查