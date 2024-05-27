# LeetCode 56 Merge Intervals
Given an array of `intervals` where `intervals[i] = [start_i, end_i]`, merge all overlapping intervals, and return *an array of the non-overlapping intervals that cover all the intervals in the input*.

Example 1:
```
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
```

Example 2:
```
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
```

Constraints:

- `1 <= intervals.length <= 10^4`
- `intervals[i].length == 2`
- `0 <= start_i <= end_i <= 10^4`

## Topic
- Array
- Sorting

## My Thinking
由於題目說給的 `Input` 是非連續的，且又要我們確認這裡面有哪些區間有重疊，因此解題思路就是先將此 `Input` 進行以各區間開頭數值進行排序。

- 首先會先給定起點和終點兩變數為第一個 `Input` 的區間。
- 接下來就是從 `Input` 的第二個區間開始一個一個判斷，會有2個判斷。
  - 此區間的起點是否 `在前區間(先前紀錄的起點和終點)內`，以及 `終點是否 > 前區間`。<br>因此需要更新前區間的終點至此區間的終點，因為這2個區間已經重疊了。<br>至於不需要探討此區間起點是否會小於前區間是因為已經先排列完畢，因此 `此區間的起點一定會 >= 前區間起點`。
  - `此區間起點 > 前區間終點`，表示此區間 `並沒有與前區間重疊`。

另外，**NeetCode** 的寫法更為簡潔清晰，可以參考。

> 參考影片: **By NeetCode**
>
> `Time complexity = O(nlogn), Space complexity = O(n)`
> 
> [![Merge Intervals - Sorting - Leetcode 56](https://img.youtube.com/vi/44H3cEC2fFM/hqdefault.jpg)](https://www.youtube.com/watch?v=44H3cEC2fFM)


### Complexity
Time complexity: $O(nlogn)$
> 因為有使用到排序，儘管後面是使用遍歷的方式 `O(n)`，但因為只要進行排序 `Time complexity = O(nlogn)`，而 `O(nlogn) > O(n)`，因此為 **$O(nlogn)$**

Space complexity: O(n)
> 因為在輸出更新完的區間時，使用額外空間去儲存此新區間的陣列，因此為 **O(n)**。