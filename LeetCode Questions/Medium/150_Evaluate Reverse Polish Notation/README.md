# LeetCode 150 Evaluate Reverse Polish Notation
You are given an array of strings tokens that represents an arithmetic expression in a [Reverse Polish Notation](https://en.wikipedia.org/wiki/Reverse_Polish_notation).

Evaluate the expression. Return *an integer that represents the value of the expression*.

*Note* that:

- The valid operators are `'+'`, `'-'`, `'*'`, and `'/'`.
- Each operand may be an integer or another expression.
- The division between two integers always **truncates toward zero**.
- There will not be any division by zero.
- The input represents a valid arithmetic expression in a reverse polish notation.
- The answer and all the intermediate calculations can be represented in a **32-bit** integer.

Example 1:
```
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
```

Example 2:
```
Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
```

Example 3:
```
Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
```

Constraints:

- `1 <= tokens.length <= 10^4`
- `tokens[i]` is either an operator: `"+"`, `"-"`, `"*"`, or `"/"`, or an integer in the range `[-200, 200]`.

## Topic
- Math
- Array
- Stack

## My Thinking
在撰寫此題時需要先了解 [**Reverse Polish Notation**](https://en.wikipedia.org/wiki/Reverse_Polish_notation) 的規則。

根據 Wikipedia 的說法，此表示法是一種數學表示法，被稱為**字尾表示法**、**後序表示法**。<br>在1960和1970年代，此表示法廣泛地被用於台式計算機上。

此表示法為 `運算子置於運算元的後面`。<br>
ex: `三加四` = `34+` ≠ `3+4`。

因此若根據題目的example2 = ["4","13","5","/","+"]，轉換成數學式 = `(4 + (13 / 5))`。

---

另外題目還提供了3個非常重要的情報:
1. 兩個數字相除時不會發生無效除法 => `不會有除0的情況發生`。
2. 當兩數相除時直接無條件捨去取整數值(truncates toward zero)。
3. 此題目只會有 `'+'`, `'-'`, `'*'`, `'/'` 這4個運算符。

原先還在苦惱如果表示法一多，要如何透過程式轉換成數學式，多虧 **NeetCode** 的提示才終於知道該如何寫。

此題撰寫的關鍵就在使用 `Stack` 資料結構。<br>並且按照此表示法的特性，在處理運算符的時候一定會有兩個運算子。

因此此題的關鍵就是遇到數字就通通塞進 `Stack` 中，直到遇到運算符。<br>遇到運算符時就是把 `Stack` 中的最後2個數字進行運算後再加入回`Stack` 中。<br>就這樣一直重複直到陣列遍歷完畢，`Stack` 中就只會剩下所有運算的結果。

另外在撰寫判斷是否遇到運算符時，需要注意不能寫成 `not in ['+', '-', '*', '/']`，因為在 `Python陣列中`，此方法會是 `Time complexity = O(m)`。<br>最好的寫法就是一個一個運算符去判斷，或是將這4個運算符改成 `Set` 資料結構，這樣在判斷 `not in` 時就只會是 `Time complexity = O(1)`。

> 參考影片: **By NeetCode**
>
> `Time complexity = O(n), Space complexity = O(n)`
> 
> [![Evaluate Reverse Polish Notation - Leetcode 150 - Python](https://img.youtube.com/vi/iu0082c4HDE/hqdefault.jpg)](https://www.youtube.com/watch?v=iu0082c4HDE)


### Complexity
Time complexity: O(n)
> 因為在進行 `Reverse Polish Notation` 的解碼並計算時使用 `迴圈進行遍歷`，因此為 **O(n)**

Space complexity: O(n)
> 因為額外使用 `Stack陣列` 紀錄當前數學運算結果，因此為 **O(n)**。