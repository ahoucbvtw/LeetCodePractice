# LeetCode 704 Binary Search

Given an array of integers `nums` which is sorted in ascending order, and an integer `target`, write a function to search `target` in `nums`. 

If `target` exists, then return its index. Otherwise, return `-1`.

You must write an algorithm with `O(log n)` runtime complexity.



Example 1:

```
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
```

Example 2:

```
Input: nums = [-1,0,3,5,9,12], target = 2
> Output: -1
> Explanation: 2 does not exist in nums so return -1
```

Constraints:

- `1 <= nums.length <= 10^4`
- `-10^4 < nums[i], target < 10^4`
- All the integers in `nums` are **unique**.
- `nums` is sorted in ascending order.

## Topic
- Array
- Binary Search

## My Thinking
題目明確標示撰寫一演算法符合`O(log n)`的時間複雜度

且題目敘述中也說明此陣列是經過排序<br>
因此使用`Binary Search 二分搜尋法`

***

建立頭尾指針 `i,k`

頭指針位置為陣列開頭 `index=0`<br>
尾指針位置為陣列最後 `index=len(Array)-1`

接著按照2分搜尋法的原則，每次搜尋陣列的中間位置 `mid= (i + k) // 2`

1. 若此次的 `Array[mid] < target`<br>頭指針 `i` 的位置需要往後更新至 `mid + 1` 的位置<br>此時下次搜尋中間位置時就會是 `mid = ((mid + 1)+ k) // 2`
2. 若此次的 `Array[mid] > target`<br>尾指針 `k` 的位置需要往前更新至 `mid - 1` 的位置<br>此時下次搜尋中間位置時就會是 `mid = (i + (mid - 1)) // 2`
3. 若此次的`Array[mid] == target`<br>表示找到目標直接輸出 `mid` 值
4. 最後若是 `i = k` 的情況發生，也是需要判斷2種狀況
   1. `Array[mid] == target`<br>表示找到目標直接輸出 `mid` 值
   2. `Array[mid] != target`<br>表示此陣列並未找到任何與 `target` 相同值，因此按照題目要求輸出 `-1`