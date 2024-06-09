# LeetCode 19 Remove Nth Node From End of List
Given the `head` of a linked list, remove the `nth` node from the end of the list and return its head.

Example 1:

![example1](https://assets.leetcode.com/uploads/2020/10/03/remove_ex1.jpg)

```
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
```

Example 2:
```
Input: head = [1], n = 1
Output: []
```

Example 3:
```
Input: head = [1,2], n = 1
Output: [1]
```

Constraints:

- The number of nodes in the list is `sz`.
- `1 <= sz <= 30`
- `0 <= Node.val <= 100`
- `1 <= n <= sz`

Follow up: Could you do this in one pass?

## Topic
- Linked List
- Two Pointers

## My Thinking
此題目要求將從提供的 `Linked List` 從 `後面` 開始算起 `第n個節點` 刪除，並非從頭開始算。<br>而就因為這個緣故，就變得稍微麻煩一點。

解題思路：
1. 建立一虛擬的節點 `dummy`，並且使用 `Two Pointers`，`a_point 和 cur` 兩個點皆在此 `dummy節點` 上。
2. 剛開始只有 `cur點` 一直移動直到 `cur點` 已經 `向前n步` 後，`a_point` 就可以跟著一起移動直到 `cur = None`。
3. 當迴圈結束時，`a_point` 就會位於 `要刪除節點的前一個節點`，因此最後只需要將 `a_point.next 設置成 a_point.next.next`，就完成此 `Linked List` 刪除從 `後面` 開始算起 `第n個節點`。

### Complexity
Time complexity: O(n)
> 因為使用迴圈進行完整 `Linked List` 的遍歷，因此為 **O(n)**

Space complexity: O(1)
> 在解題的過程中並未需要迭代的額外空間進行儲存，因此為 **O(1)**。