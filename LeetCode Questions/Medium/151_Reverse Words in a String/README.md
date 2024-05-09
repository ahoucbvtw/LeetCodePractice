# LeetCode 151 Reverse Words in a String
Given an input string `s`, reverse the order of the words.

A word is defined as a sequence of non-space characters. The **words** in `s` will be separated by at least one space.

Return *a string of the words in reverse order concatenated by a single space*.

Note that `s` may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

Example 1:
```
Input: s = "the sky is blue"
Output: "blue is sky the"
```

Example 2:
```
Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
```

Example 3:
```
Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
```

Constraints:

- `1 <= s.length <= 10^4`
- `s` contains English letters (upper-case and lower-case), digits, and spaces `' '`.
- There is **at least one** word in s.

Follow-up: If the string data type is mutable in your language, can you solve it in-place with `O(1)` extra space?

## Topic
- String
- Two Pointers

## My Thinking
此題非常簡單，由於題目需要將字串反轉，但字串內的單字不反轉且裡面每個單字間只能有一個空格。

因此解題思路就是：
1. 去除空格製作陣列
2. 將陣列反轉並輸出文字(每個單字之間需要加空格，頭尾不需要)

### Complexity
Time complexity: O(n)
> 因為使用 `for迴圈` 進行反向遍歷輸出字串，因此為**O(n)**

Space complexity: O(n)
> 因為使用了 `split()` 製作額外記憶體空間，且在最後輸出解答時也是利用 `for迴圈` 方式反向遍歷輸出字串，因此為**O(n)**