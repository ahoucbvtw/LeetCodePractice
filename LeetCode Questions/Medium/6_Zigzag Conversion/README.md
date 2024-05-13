# LeetCode 6 Zigzag Conversion
The string `"PAYPALISHIRING"` is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

```
P   A   H   N
A P L S I I G
Y   I   R
```
And then read line by line: `"PAHNAPLSIIGYIR"`

Write the code that will take a string and make this conversion given a number of rows:

`string convert(string s, int numRows);`

Example 1:
```
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
```

Example 2:
```
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
```

Example 3:
```
Input: s = "A", numRows = 1
Output: "A"
```

Constraints:

- `1 <= s.length <= 1000`
- `s` consists of English letters (lower-case and upper-case), `','` and `'.'`.
- `1 <= numRows <= 1000`

## Topic
- String

## My Thinking
題目說要將指定字串改成符合 `numRows` 行數的 [`zigzag格式`](https://dictionary.cambridge.org/ja/dictionary/english-chinese-traditional/zigzag#google_vignette) 輸出。

首先先畫圖，以 `numRows = 4` 為例子。藍色區域為一個 `zigzag` 循環。

![numRows=4，一個zigzag循環](https://github.com/ahoucbvtw/LeetCodePractice/blob/main/LeetCode%20Questions/Medium/6_Zigzag%20Conversion/pic/6-0.png?raw=true)

接著分析每一排的規律：

第一排、最後一排(Row = 0,3)：可以發現第一排及最後一排若要獲得下一個字串，需要往前算 `第6個`，而此時也可以拆分成 `2個3 (3 * 2)`。<br>此時也可以看做 `(4 - 1) * 2 => (numRows - 1) * 2`。

![第一排](https://github.com/ahoucbvtw/LeetCodePractice/blob/main/LeetCode%20Questions/Medium/6_Zigzag%20Conversion/pic/6-1.png?raw=true)

![最後一排](https://github.com/ahoucbvtw/LeetCodePractice/blob/main/LeetCode%20Questions/Medium/6_Zigzag%20Conversion/pic/6-2.png?raw=true)

至於其他排(Row = 1~2)：仔細看會發現他們除了與第一排和最後一排有一樣的共通規律外，以箭頭的字串為例開始看一個循環，還會有額外一個字串 `(紅圈處)`。因此需要找尋此字串的規律。

![其他排的特例規律](https://github.com/ahoucbvtw/LeetCodePractice/blob/main/LeetCode%20Questions/Medium/6_Zigzag%20Conversion/pic/6-3.png?raw=true)

仔細觀察後可以發現，多出來的值，似乎可以用一個循環的 `總步數 - 定值`。

`Row = 1`: <br>`6 - 2` => `[(4 - 1) * 2] - 2` => `[(numRows - 1) * 2] - 2`。

![其他排的特例規律1](https://github.com/ahoucbvtw/LeetCodePractice/blob/main/LeetCode%20Questions/Medium/6_Zigzag%20Conversion/pic/6-4.png?raw=true)

`Row = 2`: <br>`6 - 4` => `[(4 - 1) * 2] - 4` => `[(numRows - 1) * 2] - 4`。

![其他排的特例規律2](https://github.com/ahoucbvtw/LeetCodePractice/blob/main/LeetCode%20Questions/Medium/6_Zigzag%20Conversion/pic/6-5.png?raw=true)

此時根據上2張圖，又可以得出其他排的另一個多出來字串的規律如下。

`Row = 1`: <br>`6 - 2` => `[(4 - 1) * 2] - 2` => `[(numRows - 1) * 2] - (2 * 1)` => `[(numRows - 1) * 2] - (2 * Row)`。

`Row = 2`: <br>`6 - 4` => `[(4 - 1) * 2] - 4` => `[(numRows - 1) * 2] - (2 * 2)` => `[(numRows - 1) * 2] - (2 * Row)`。
<br><br>
> 參考影片: **By NeetCode**
>
> `Time complexity = O(mn), Space complexity = O(1)`
> 
> [![ZigZag Conversion - Leetcode 6 - Python](https://img.youtube.com/vi/Q2Tw6gcVEwc/hqdefault.jpg)](https://www.youtube.com/watch?v=Q2Tw6gcVEwc)

### Complexity
Time complexity: O(mn)
> 因為使用了2個不同長度的 `for迴圈` 進行遍歷，因此為**O(mn)**

Space complexity: O(n)
> 因為使用了 `for迴圈` 進行字串的輸出，因此為**O(1)**