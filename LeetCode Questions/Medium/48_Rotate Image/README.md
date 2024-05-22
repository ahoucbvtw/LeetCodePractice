# LeetCode 48 Rotate Image
You are given an `n x n` 2D `matrix` representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. **DO NOT** allocate another 2D matrix and do the rotation.

Example 1:

![Example1](https://assets.leetcode.com/uploads/2020/08/28/mat1.jpg)

```
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
```

Example 2:

![Example2](https://assets.leetcode.com/uploads/2020/08/28/mat2.jpg)

```
Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
```

Constraints:

- `n == matrix.length == matrix[i].length`
- `1 <= n <= 20`
- `-1000 <= matrix[i][j] <= 1000`

## Topic
- Math
- Array
- Matrix

## My Thinking
`48_1.py` 的解題思路：
- 透過對原矩陣取轉置矩陣最後再進行鏡像翻轉。
- 鏡像翻轉時需要考慮此正方矩陣的邊長是奇數還是偶數。<br>奇數：鏡像時會剛好只有中間排沒有對象鏡像。<br>偶數：剛好全部都可以進行鏡像翻轉。

![鏡像_奇數](https://github.com/ahoucbvtw/LeetCodePractice/blob/main/LeetCode%20Questions/Medium/48_Rotate%20Image/pic/3.PNG?raw=true)

![鏡像_偶數](https://github.com/ahoucbvtw/LeetCodePractice/blob/main/LeetCode%20Questions/Medium/48_Rotate%20Image/pic/2.PNG?raw=true)

---

`48_2.py` 參考了 `NeetCode` 的解題思路：
- 若進行順時針旋轉90°，先觀察4個角落，再觀察其他地方。<br>可以發現原先 `左上的值換到右上的值`，`右上換到右下`，`右下換到左下`，`左下換到左上`。<br>簡單來說就是 `上邊換到右邊`，`右邊換到下邊`，`下邊換到左邊`，`左邊換到上邊`。
- 利用上面特性，設置4個指標，`TBLR` 分別代表 `上下左右`。
- 因題目要求不能額外輸出一個新矩陣，所以只能去更改原矩陣。<br>但是若使用上面特性一個一個換的話，到最後會遺漏值。<br>因此再設置一個可以暫存第一個準備要交換的值的變數 `temp`。
- 交換時從左上開始，先把 `左上給temp`，此時左上已經隨時準備好被其他值給覆蓋。<br>而根據第一點的觀察，`左上會被左下的值覆蓋`，而 `左下又會被右下覆蓋`，依此類推下去可以發現，在交換值的時候會是 `逆時針` 進行交換。
- 當最外圈都旋轉完後就慢慢向內一層一層進行旋轉 `L += 1, R -= 1`，直到 `L >= R` 為止。

![逆時針交換](https://github.com/ahoucbvtw/LeetCodePractice/blob/main/LeetCode%20Questions/Medium/48_Rotate%20Image/pic/1.PNG?raw=true)

> 參考影片: **By NeetCode**
>
> `Time complexity = O(n^2), Space complexity = O(1)`
> 
> [![Rotate Image - Matrix - Leetcode 48](https://img.youtube.com/vi/fMSJSS7eO1w/hqdefault.jpg)](https://www.youtube.com/watch?v=fMSJSS7eO1w)


### Complexity
Time complexity: $O(n^2)$
> 不管是 `48_1.py` 或 `48_2.py` 都是需要遍歷全部的2維陣列才能將他們全部做順時針選轉90°，因此為 **$O(n^2)$**

Space complexity: O(1)
> 不管是 `48_1.py` 或 `48_2.py` 都是從頭到尾都並沒有進行 `迭代` 的額外空間儲存，只有 `將指定位置的矩陣值放入另一個指定位置而已`，因此為 **O(1)**。