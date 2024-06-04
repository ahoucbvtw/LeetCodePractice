# LeetCode 21 Merge Two Sorted Lists
You are given the heads of two sorted linked lists `list1` and `list2`.

Merge the two lists into one **sorted** list. The list should be made by splicing together the nodes of the first two lists.

Return *the head of the merged linked list*.

Example 1:

![example](https://assets.leetcode.com/uploads/2020/10/03/merge_ex1.jpg)

```
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
```

Example 2:
```
Input: list1 = [], list2 = []
Output: []
```

Example 3:
```
Input: list1 = [], list2 = [0]
Output: [0]
```

Constraints:

- The number of nodes in both lists is in the range `[0, 50]`.
- `-100 <= Node.val <= 100`
- Both `list1` and `list2` are sorted in non-decreasing order.

## Topic
- Recursion
- Linked List

## My Thinking
此題為經典的鏈結串列的插入題型。鏈結串列在插入時操作與陣列不同，無法知道要插入的位置，因此必須要全部遍歷一遍。

而此題關鍵就在需要建立一個新的空節點，並將此節點當作用來接續接下來判斷2鏈結串列大小排序。<br>不要將空此節點當作最後要輸出的鏈結串列的 `head`，因為會變的綁手綁腳不好操作，統一於新空節點的下一個節點來判斷要新增哪一個節點。

另外，題目也有說明提供的2個鏈結串列都已經是經過 `升序` 排序過，因此在融合時不需要擔心後面的節點比前面還小。

因此解題思路：
1. 建立一個空節點，並將此空節點當作要輸出成答案的虛擬鏈結串列頭。
2. 題目給的2個鏈結串列頭值有2種判斷：
   1. `list1.val < list2.val`。<br>將較小的串在當前空節點的鏈結串列的下一個位置。
   2. `list1.val >= list2.val`。<br>直接將 `list2` 串在當前空節點的鏈結串列的下一個位置。
3. 當 `while迴圈` 停止時 = 其中一個鏈結串列當前節點已經是空值。<br>但是還必須防止如果2個鏈結串列長度不一樣長時，此時會導致漏掉另一邊剩餘的節點。<br>因此最後要加入判斷是哪一個提供的鏈結串列當前節點為空，並將另一個剩餘的節點給全部加入空節點的鏈結串列。<br>至於為什麼可以這樣操作的原因在於題目已經明確說明提供的鏈結串列都是已經按照 `升序` 排序，因此剩餘的鏈結串列節點變不需要再進行比對，可以直接加入在空節點的鏈結串列中。

> 參考影片: **By Greg Hogg**
>
> `Time complexity = O(n), Space complexity = O(1)`
> 
> [![Merge Two Sorted Lists - Leetcode 21 - Linked Lists (Python)](https://img.youtube.com/vi/5Rec4JS9H5o/hqdefault.jpg)](https://www.youtube.com/watch?v=5Rec4JS9H5o)

### Complexity
Time complexity: O(n)
> 因為在進行2個鏈結串列合併時需要進行全部節點的遍歷，但又因為若2個鏈結串列長度不同時，按照寫法只會遍歷完短的，因此為 **O(n)**

Space complexity: O(1)
> 就算額外使用空間去紀錄新的空鏈結串列的節點，在題目的操作上也只是去操作他的next值，並不會因此而儲存到 `O(n)` 的空間，因此為 **O(1)**。