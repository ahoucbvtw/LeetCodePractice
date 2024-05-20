# LeetCode 54 Spiral Matrix
Given an` m x n` `matrix`, return *all elements of the `matrix` in spiral order*.

Example 1:

![example1](https://assets.leetcode.com/uploads/2020/11/13/spiral1.jpg)

```
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
```

Example 2:

![example2](https://assets.leetcode.com/uploads/2020/11/13/spiral.jpg)

```
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
```

Constraints:

- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 10`
- `-100 <= matrix[i][j] <= 100`

## Topic
- Array
- Matrix
- Simulation

## My Thinking
根據 `NeetCode影片提示`，此題可以使用 `Two Pointers` 的變形，我稱為 `Four Pointers`。<br>從名字就可以看出是使用 `4個點`，然後逐一縮減範圍，直到相等或超過。

題目要求輸出一組2維陣列按照從左上開始順時針一直繞到裡面直到全部的2維陣列值都遍歷完畢。

因此解題思路：
- 創建上下左右4個點位，其中 `上、左 = 0`，`下、右 = 2維陣列的y和x長度`
  - ex: matrix = [ [2,5,8], [4,0,-1] ], 下指標 = 2, 右指標 = 3<br>至於為什麼不是 `長度 - 1` 的原因是後續使用 `for迴圈` 方便撰寫。
- 若進行順時針繞，可以拆分成4個動作一直循環直到全部遍歷完畢：
  - `上面(紅色)：左 -> 右。`<br>當此動作完成後需要將 `上指標向下移動一格`，因為接下來要換遍歷右邊。<br>但是題目又要求不能重複，因此需要在遍歷右邊前將 `上指標向下移動一格`。<br><br>
  - `右邊(紫色)：上 -> 下。`<br>當此動作完成後需要將 `右指標向左移動一格`，因為接下來要換遍歷下面。<br>但是題目又要求不能重複，因此需要在遍歷下面前將 `右指標向左移動一格`。<br><br>
  - `下面(藍色)：右 -> 左。`<br>當此動作完成後需要將 `下指標向上移動一格`，因為接下來要換遍歷左邊。<br>但是題目又要求不能重複，因此需要在遍歷左邊前將 `下指標向上移動一格`。<br><br>
  - `左邊(綠色)：下 -> 上。`<br>當此動作完成後需要將 `左指標向右移動一格`，因為此時一個順時針輪回已經結束要繼續第2輪的上面。<br>但是題目又要求不能重複，因此需要在遍歷第2輪上面前將 `左指標向右移動一格`。<br><br>
  
    ![順時針循環繞](https://github.com/ahoucbvtw/LeetCodePractice/blob/main/LeetCode%20Questions/Medium/54_Spiral%20Matrix/pic/1.png?raw=true)
- 另外在順時針繞時，還需要在繞完 `上面以及右邊` 後加入判斷此2維陣列是否屬於 `1 x n` 或 `n x 1`。<br>因為這兩種情形是不需要再繼續遍歷後2個動作，已經在前2個動作就全部遍歷完畢，因此要提前結束迴圈。


> 參考影片: **By NeetCode**
>
> `Time complexity = O(mn), Space complexity = O(1)`
> 
> [![Spiral Matrix - Microsoft Interview Question - Leetcode 54](https://img.youtube.com/vi/BJnMZNwUk1M/hqdefault.jpg)](https://www.youtube.com/watch?v=BJnMZNwUk1M)


### Complexity
Time complexity: O(mn)
> 由於此題目是需要遍歷全部的2維陣列，但2維陣列大小又是不固定，因此為 **$O(mn)$**

Space complexity: O(1)
> 由於從頭到尾都並沒有進行額外空間的儲存，只有 `獲取指定位置的2維陣列值`，因此為 **O(1)*。