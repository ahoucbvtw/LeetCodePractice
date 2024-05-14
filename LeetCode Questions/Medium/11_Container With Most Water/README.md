# LeetCode 11 Container With Most Water
You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `ith` line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return *the maximum amount of water a container can store*.

**Notice** that you may not slant the container.

Example 1:

![11_example1](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg)
```
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
```

Example 2:
```
Input: height = [1,1]
Output: 1
```

Constraints:

- `n == height.length`
- `2 <= n <= 10^5`
- `0 <= height[i] <= 10^4`

## Topic
- Array
- Greedy
- Two Pointers

## My Thinking
由於題目很佛心，計算最大注水面積時 `只能是水平，不能有任何傾斜`。因此只需要考慮 `矩形面積(長 * 寬)的最大值` 即可。

至於對應此題要求的矩形面積長與寬分別代表如下：<br>長 => `選定的2個直線其最矮的高度(因為不能有任何傾斜，所以只能選較矮的高度)`<br>寬 => `選定的2個直線之間的距離(X軸相差的距離)`

而為了獲得最大面積，長與寬都要是最大，因此這裡使用 `Two Pointers`。<br>最先藉由左邊點設置在陣列開頭，右邊點設置在陣列尾部，獲得最大的寬，並慢慢向中間靠攏計算最大面積。

至於向中間移動的條件如下：
- 當右邊點位值 >= 左邊點位值 : `左邊點位向前一步`
  - 為什麼要判斷 `=`，是因為即使左右兩邊相等，若陣列還沒確實計算完畢，可能會漏掉最大面積。
  - 不過其實 `=` 判斷放在這邊或下面都沒有差別。
- 當右邊點位值 < 左邊點位值 : `右邊點位向後一步`

### Complexity
Time complexity: O(n)
> 因為使用 `while迴圈` + `Two Pointers` 進行全部陣列的遍歷，因此為**O(n)**

Space complexity: O(1)
> 在2條線的高度獲取上由於是直接從 `陣列中指定位置取得`，因此為**O(1)**