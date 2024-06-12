# LeetCode 86 Partition List
Given the `head` of a linked list and a value `x`, partition it such that all nodes **less than** `x` come before nodes **greater than or equal** to `x`.

You should **preserve** the original relative order of the nodes in each of the two partitions.

Example 1:

![example1](https://assets.leetcode.com/uploads/2021/01/04/partition.jpg)

```
Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]
```

Example 2:

```
Input: head = [2,1], x = 2
Output: [1,2]
```

Constraints:

- The number of nodes in the list is in the range `[0, 200]`.
- `-100 <= Node.val <= 100`
- `-200 <= x <= 200`

## Topic
- Linked List
- Two Pointers

## My Thinking
此題目是要求將給定的 `鏈結串列個節點值與x比大小`，要 `將所有 < x 的節點值放在所有 > x 的節點值前面`，並且各自需要先進行串列。

因此參考 **NeetCode** 的原理解說後，此題的解題步驟如下：
1. 首先建立 `左邊與右邊的dummy節點`，並且設置 `左邊與右邊的cur(left_tail, right_tail)`。
2. 按照題目所說，遍歷鏈結串列並與 `x` 比大小。<br> `< x 放進左邊鏈結串列`，`> x 放進右邊鏈結串列`。
3. 當全部遍歷完畢後 `left_tail, right_tail` 也剛好是各自鏈結串列的最尾端。<br>此時只需要將 `左邊鏈結串列尾端連接右邊鏈結串列頭`，且 `右邊鏈結串列尾連接None`，就完成題目要求。

> 參考影片: **By NeetCode**
>
> `Time complexity = O(n), Space complexity = O(1)`
> 
> [![Partition List - Linked List - Leetcode 86](https://img.youtube.com/vi/KT1iUciJr4g/hqdefault.jpg)](https://www.youtube.com/watch?v=KT1iUciJr4g)


### Complexity
Time complexity: O(n)
> 因為使用迴圈進行遍歷全部鏈結串列，因此為 **O(n)**

Space complexity: O(1)
> 雖然左右兩邊鏈結串列看似在迭代串接，但因為資料型態是鏈結串列，都是以節點串節點的方式呈現，並非像陣列中的迭代新增值，因此為 **O(1)**。