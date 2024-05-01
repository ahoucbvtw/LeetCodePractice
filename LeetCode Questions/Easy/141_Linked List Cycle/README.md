# LeetCode 141 Linked List Cycle
Given `head`, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer. Internally, `pos` is used to denote the index of the node that tail's `next` pointer is connected to. **Note that `pos` is not passed as a parameter**.

Return `true` if there is a cycle in the linked list. Otherwise, return `false`.

Example 1:

![Example_1](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist.png)
```
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
```

Example 2:

![Example_2](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test2.png)
```
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
```

Example 3:

![Example_3](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test3.png)
```
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
```

Constraints:

- The number of the nodes in the list is in the range `[0, 10^4]`.
- `-10^5 <= Node.val <= 10^5`
- `pos` is `-1` or a **valid index** in the linked-list.

Follow up: Can you solve it using `O(1)` (i.e. constant) memory?

## Topic
- Hash Table
- Linked List
- Two Pointers

## My Thinking
因為題目說 `pos` 是此 `Linked List` 往前循環的節點位置，但是在寫程式做判斷的時候不能使用它來判斷題目是否給的是一個有循環的 `Linked List`。

因此這裡使用 `Two Pointers` 的一種: 快慢指針 `Fast-slow Pointers` == 龜兔演算法 `Hare & Tortoise Algorithm`。

此演算法是利用一個前進較快的指針與一格一格前進的指針去執行，而為什麼此演算法可以找到是否是循環的 `Linked List` 原因在於，只要是循環，快指針不管如何都一定會超過慢指針一圈，**且2者定會在某個時間點重合**。<br>因此只需要利用搜尋快慢2指針是否在一樣的節點上即表示此 `Linked List` 為循環。


> 詳細解說影片 By: **Algo Engine**
>
> [![LeetCode #141: Linked List Cycle | Floyd's Tortoise and Hare Algorithm](https://i.ytimg.com/vi/RRSItF-Ts4Q/hqdefault.jpg?sqp=-oaymwEcCNACELwBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLDljxLl_Eqvba7LjH_BSO78xuGqlQ)](https://www.youtube.com/watch?v=RRSItF-Ts4Q)


### Complexity
Time complexity: O(n)
> 因此使用 `Fast-slow Pointers` 方法搜尋是否有此 `Linked List` 有循環，若最壞的情況是快指針及慢指針都循環了2-3次才碰面，代表跑了 `2n or 3n`，但是在計算 `Time complexity` 時常數項可以忽略，因此為 **O(n)**

Space complexity: O(1)
> 因為此題都是明確判斷及指定節點位置 `(head = head.next, fast = fast.next.next)` ，因此為 **O(1)**