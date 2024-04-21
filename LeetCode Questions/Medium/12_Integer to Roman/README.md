# LeetCode 12 Integer to Roman
Roman numerals are represented by seven different symbols: `I`, `V`, `X`, `L`, `C`, `D` and `M`.

```
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
```

For example, `2` is written as `II` in Roman numeral, just two one's added together. `12` is written as `XII`, which is simply `X + II`. The number `27` is written as `XXVII`, which is `XX + V + II`.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not `IIII`. Instead, the number four is written as `IV`. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as `IX`. There are six instances where subtraction is used:

- `I` can be placed before `V` (5) and `X` (10) to make 4 and 9. 
- `X` can be placed before `L` (50) and `C` (100) to make 40 and 90. 
- `C` can be placed before `D` (500) and `M` (1000) to make 400 and 900.

Given an integer, convert it to a roman numeral.

Example 1:
```
Input: num = 3
Output: "III"
Explanation: 3 is represented as 3 ones.
```

Example 2:
```
Input: num = 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.
```

Example 3:
```
Input: num = 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
```

Constraints:

- `1 <= num <= 3999`

## Topic
- Hash Table
- Math
- String

## My Thinking
羅馬數字有一些規則，**只有7個符號**: `I=1，V=5，X=10，L=50，C=100，D=500，M=1000`<br>**羅馬數字沒有0的符號**
- 重複次數決定倍數: 
  - 1個羅馬數字重複幾次，就表示這個數的幾倍<br>ex: `XXX=30`
- 右加左減:
  - 大羅馬數字的右邊＋小羅馬數字 => 加法<br> ex: `XII = 10 + 1 + 1`
  - 大羅馬數字的左邊+小羅馬數字 => 減法(大-小)<br> ex: `XIV = 10 + (5 - 1)`
  - 左減不能跨過一位數<br> ex: `99 != IC` 而是 `XCIX = (100 - 10) + (10 - 1)`
  - 左減不能超過1個，右加不能超過3個<br> ex: `8 != IIX` 而是 `VIII`，`14 != XIIII` 而是 `XIV`
- 同樣羅馬數字最多只能出現3次<br> ex: `40 != XXXX` 而是 `XL`

> 參考資料:
>
> http://www.mathland.idv.tw/history/roman.htm

<br><br>
按照上面對於羅馬文字與數字的轉換規則

1. 首先建立一個羅馬文字與數字的對照表(Hash Table)
2. 將題目給的數字先轉成字串後取得此數字的位數
3. 根據規則可以發現當遇到數字`4,5,9`時都會有特殊規則，按照這些數字制定特殊規則<br>`4 => 5-1`, `40 => 50-10`...<br>`5 => V`, `50 => L`<br>`9 => 10-1`, `90 => 100-10`

### Complexity
Time complexity: O(n)
> 因為將是從頭到尾的一個一個去解析當下的數字屬於哪個羅馬字，所以是 **O(n)**

Space complexity: O(1)
> 每一次查詢數字的羅馬字的時候都是直接使用`Hash Table`查詢，所以是 **O(1)**