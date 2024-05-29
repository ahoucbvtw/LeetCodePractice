# LeetCode 57 Insert Interval
You are given an array of non-overlapping intervals `intervals` where `intervals[i] = [starti, endi]` represent the start and the end of the `ith` interval and `intervals` is sorted in ascending order by `start_i`. You are also given an interval `newInterval = [start, end]` that represents the start and end of another interval.

Insert `newInterval` into `intervals` such that `intervals` is still sorted in ascending order by `start_i` and `intervals` still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return `intervals` after the insertion.

Note that you don't need to modify `intervals` in-place. You can make a new array and return it.

Example 1:
```
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
```

Example 2:
```
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
```

Constraints:

- `0 <= intervals.length <= 10^4`
- `intervals[i].length == 2`
- `0 <= start_i <= end_i <= 10^5`
- `intervals` is sorted by `start_i` in ascending order.
- `newInterval.length == 2`
- `0 <= start <= end <= 10^5`

## Topic
- Array

## My Thinking
根據題目所說需要在一個排序好的陣列區間加入一新的區間，並確定此區間是否有與原區間重疊，有的話就要進行合併，沒有的話就要將此區間插入至合適的位置。

而在插入新區間時總共會有4種情況：
1. 新加入的區間最大值 < intervals內所有區間。<br>`直接在最左邊加入該區間。`<br>
2. 新加入區間最小值 > intervals內所有區間。<br>`直接在最右邊加入該區間。`<br>
3. 新加入區間在intervals內某兩區間的中間並未重疊。<br>`雖然說是在中間，但是新加入的區間的最大值也是 < 目前遍歷剩餘的區間，因此適用第1種情況。`<br>
4. 新加入區間在intervals內某n個區間重疊。<br>
  ```
  先計算第一個重疊，再看是否與下一個區間也有重疊。
  有在進行合併，沒有就將此合併新增至output。
  ```

按照上面邏輯撰寫後，由於撰寫的方式原因[57.py](https://github.com/ahoucbvtw/LeetCodePractice/blob/main/LeetCode%20Questions/Medium/57_Insert%20Interval/57.py)，最後全部區間遍歷完後還需要再加入newInterval。<br>因為當最後遍歷完後是第2或4種情況時就會少加入。

- 2的情況：新區間 > 所有原陣列區間。因為在此情況的撰寫方式是只有將前面原陣列所有區間加入output的緣故，因此需要在最後加入題目提供的newInterval。
- 4的情況：因為不確定加入的新區間是否有橫跨多個舊區間，尤其是若橫跨至最後一個時會因撰寫方式的緣故，最後還需要將合併後的區間加入。

> 參考影片: **By NeetCode**
>
> `Time complexity = O(n), Space complexity = O(n)`
> 
> [![Insert Interval - Leetcode 57 - Python](https://img.youtube.com/vi/A8NUOmlwOlM/hqdefault.jpg)](https://www.youtube.com/watch?v=A8NUOmlwOlM)


### Complexity
Time complexity: O(n)
> 因為並未使用到排序，而是一個區間慢慢遍歷檢查是否插入的區間有重疊，因此為 **O(n)**

Space complexity: O(n)
> 因為在輸出更新完的區間時，使用額外空間去儲存此新區間的陣列，因此為 **O(n)**。