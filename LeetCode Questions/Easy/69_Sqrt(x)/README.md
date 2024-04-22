# LeetCode 69 Sqrt(x)
Given a non-negative integer `x`, return *the square root of `x` rounded down to the nearest integer*. The returned integer should be **non-negative** as well.

You **must not use** any built-in exponent function or operator.

- For example, do not use `pow(x, 0.5)` in c++ or `x ** 0.5` in python.

Example 1:
```
Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
```

Example 2:
```
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
```

Constraints:

- `0 <= x <= 2^31 - 1`


## Topic
- Math
- Binary Search

## My Thinking
此題要不使用內建函數來達成平方根的演算法，並且最後輸出答案的小數點部份是`無條件捨去`，因此就只需要注意正整數

題目給定一數字`x`，因此可以想像需要從 `0 ~ x` 個數字中找出哪一個數字是最接近 `x` 的平方根

此題目有2種解法
1. 從0開始計算每個數字的平方是否接近`x`<br>但是這樣 `Time complexity = O(n)`，並非不可以只是有更好的解法
2. 使用 `Binary Search` 每次跨越一半的維度搜尋某個數字的平方是否接近`x`，也是目前使用的方法<br>此 `Time complexity = O(logn)`

### Complexity
Time complexity: O(logn)
> 使用 `Binary Search` 每次進行對半搜尋直到找到近似或一樣的值，因此為 **O(logn)**

Space complexity: O(1)
> 在使用 `Binary Search` 過程中只有針對該數字做平方的檢查，並沒有做複雜的計算，因此為 **O(1)**