# LeetCode 238 Product of Array Except Self
Given an integer array `nums`, return *an array answer such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`*.

The product of any prefix or suffix of `nums` is **guaranteed** to fit in a **32-bit** integer.

You must write an algorithm that runs in `O(n)` time and without using the **division operation**.

Example 1:
```
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
```

Example 2:
```
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
```

- 2 <= nums.length <= 10^5
- -30 <= nums[i] <= 30
- The product of any prefix or suffix of `nums` is **guaranteed** to fit in a **32-bit** integer.

Follow up: Can you solve the problem in `O(1)` extra space complexity? (The output array **does not** count as extra space for space complexity analysis.)

## Topic
- Array
- Prefix Sum

## My Thinking
參考了 `Nikhil Lohiae` 以及 `NeetCode` 影片<br>先使用 `Nikhil Lohiae` 思路製作 `238_1.py` 其 `Time complexity & Space complexity = O(n)`<br>後面藉由觀看 `NeetCode` 影片獲得該如何讓 `Space complexity = O(1)` 啟發撰寫 `238_2.py`。

解題方法:<br>題目要求在陣列內除了自身數值外其餘數值相乘並輸出且 `Time complexity = O(n)` 以及無法使用 `除法` 這2個條件。<br>`(Space complexity = O(1) 是題目額外給的挑戰)`

在迴圈上一個一個遍歷的時候，會發現除了自身以外的乘積這件事可以看成 `左邊+右邊所有數值相乘`
```
nums = [1,2,3,4]

當目前迴圈位置在 2 時，得出解 = 1x3x4
其中1相對2來說是左半邊的數字，3,4是右半邊的數字

所以此題可以看成 = 左邊+右邊所有數值相乘
```

那如果迴圈在陣列的開頭與末端時該怎麼半？<br>開頭: 因為在開頭左邊並沒有任何數值，因此當作左邊有一個數值 `1`，這樣不管如何乘都不會影響題目。<br>末端: 因為在末端右邊並沒有任何數值，因此與開頭一樣在右邊當作有一個數值 `1`。

---

### 238_1.py
在 `238_1.py`，因為知道題目可以看成 `左邊+右邊所有數值相乘`。<br>因此額外利用記憶體空間製作在陣列中每個值的左邊所有乘積以及右邊所有乘積。<br>將左右兩邊都計算完後，再按照順序左邊與右邊一個一個數值再次相乘就會得到答案

```
nums = [1, 2, 3, 4]

left = [1, 1x1, 1x1x2, 1x2x3]
right = [2x3x4, 3x4x1, 4x1, 1]
output = left x right
       = [1x2x3x4, 1x1x3x4x1, 1x1x2x4x1, 1x2x3x1]
       = [24, 12, 8, 6]
```

> 參考影片1: **By Nikhil Lohiae**
>
> `Time complexity & Space complexity = O(n)`
> 
> [![Product of Array Except Self (LeetCode 238) | Full solution with visuals | Study Algorithms](https://i3.ytimg.com/vi/G9zKmhybKBM/maxresdefault.jpg)](https://www.youtube.com/watch?v=G9zKmhybKBM)

---

### 238_2.py
在 `238_2.py` 中，因為知道題目可以看成 `左邊+右邊所有數值相乘`，且為了挑戰題目給的額外挑戰 `Space complexity = O(1)`。<br>與 `238_1.py` 不同，不使用額外記憶體空間紀錄左邊與右邊所有相乘的值。<br>因此透過2次迴圈，第1次一樣計算左邊，只是先把值寫入 `output` 內。<br>當進行第2次迴圈時，設置一個 `int right` 變數紀錄每次右邊所有數值的相乘當作 `238_1.py` 的右邊陣列<br>再與 `output` 也就是 `238_1.py` 的左邊陣列相乘，即可得出解。

利用此方法可以解放 `238_1.py` 的左右邊陣列記憶體，只需要使用一個 `int right` 變數的記憶體即可以達成一樣的效果。

```
nums = [1, 2, 3, 4]

經過一次迴圈(製作左邊數值相乘)
output = [1, 1x1, 1x1x2, 1x2x3]

設置用來紀錄每次右邊所有數值的相乘變數 int right = 1
right = 1(因為陣列最後一個值右邊並沒有值，因此給1定值)

並且經過逆迴圈將計算的右邊所有數值的相乘值(right)與 output(左邊數值相乘) 相乘
right = 1 => 4x1 => 3x4x1 => 2x3x4x1
output = [1x(right), 1x2x(right), 1x1x2x(right), 1x2x3x(right)]
       = [1x(2x3x4x1), 1x2x(3x4x1), 1x1x2x(4x1), 1x2x3x(1)]
       = [24, 12, 8, 6]
```

> 參考影片2: **By NeetCode**
>
> `Time complexity = O(n) / Space complexity = O(1)`
> 
> [![Product of Array Except Self - Leetcode 238 - Python](https://i.ytimg.com/vi/bNvIQI2wAjk/hqdefault.jpg)](https://www.youtube.com/watch?v=bNvIQI2wAjk)


### Complexity
Time complexity: O(n)
> 因為都只有使用 `for迴圈` 進行遍歷計算左右邊數值相乘，因此為**O(n)**

Space complexity: O(n)、O(1)
> 在 `238_1.py` 因為使用2個陣列去額外儲存左右邊數值相乘的值，因此為**O(n)**
> 
> 在 `238_2.py` 因為並未使用陣列去額外儲存，只有使用 `int 變數`，因此為**O(1)**