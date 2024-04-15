# LeetCode 88 Merge Sorted Array

You are given two integer arrays `nums1` and `nums2`, sorted in **non-decreasing order**, and two integers `m` and `n`, representing the number of elements in `nums1` and `nums2` respectively.

**Merge** `nums1` and `nums2` into a single array sorted in **non-decreasing order**.

The final sorted array should not be returned by the function, but instead be stored inside the array `nums1`.<br>To accommodate this, `nums1` has a length of `m + n`, where the first m elements denote the elements that should be merged, and the last `n` elements are set to `0` and should be ignored. `nums2` has a length of `n`.

Example 1:

```
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]

Explanation: 
The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
```

Example 2:

```
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]

Explanation: 
The arrays we are merging are [1] and [].
The result of the merge is [1].
```

Example 3:

```
Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: 
The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. 
The 0 is only there to ensure the merge result can fit in nums1.
```

Constraints:

- `nums1.length == m + n`
- `nums2.length == n`
- `0 <= m, n <= 200`
- `1 <= m + n <= 200`
- `-10^9 <= nums1[i], nums2[j] <= 10^9`

**Follow up**: Can you come up with an algorithm that runs in `O(m + n)` time?

## Topic
- Array
- Two Pointers
- Sorting

## My Thinking

### GIF
> Thanks to BigMangos for the GIF that make me understand how to solve this question.
> 
> ![GIF](https://i.loli.net/2019/05/14/5cdac3209479073662.gif)

### Text
題目要將2個陣列比大小後又重新排列，因此屬於merge sort<br>
但又因為題目**必須要直接更改nums1的方式**，而不是輸出新的陣列<br>
因此**需要3個變數**<br>
1. index = m+n-1 = 兩個陣列加起來後的最後一個index<br>
2. a_index = m - 1 = nums1陣列尚未加總前的最後一個有數字的index<br>
3. b_index = n - 1 = nums2陣列的最後一個index

**nums1陣列會在前方有m的數量後其餘補n個0**<br>
也就是nums1前面會有m個數字，然後剩餘都是n個0<br>
ex: m = 3, n = 4, nums1 = [-1, 2, 4, 0, 0, 0, 0]

因為nums1有後面補0的特性，所以需要從nums1最後面一個一個向前比大小放入排序好的數字<br>
直到b_index = 0, 也就是直到比較到nums2第一個數字比完才停止<br>而比較的時候也是從nums1, nums2的最後一個開始比

當a_index >= 0 和 nums1[a_index] > nums2[b_index]時<br>把 nums1[a_index] 放置 nums1[index]<br>
此時a_index - 1<br>
其餘則直接把 nums2[b_index] 放置 nums1[index](包含a_index < 0)<br>並將b_index - 1