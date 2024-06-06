# LeetCode 138 Copy List with Random Pointer
A linked list of length `n` is given such that each node contains an additional random pointer, which could point to any node in the list, or `null`.

Construct a [deep copy](https://en.wikipedia.org/wiki/Object_copying#Deep_copy) of the list. The deep copy should consist of exactly `n` **brand new** nodes, where each new node has its value set to the value of its corresponding original node. Both the `next` and `random` pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. **None of the pointers in the new list should point to nodes in the original list**.

For example, if there are two nodes `X` and `Y` in the original list, where `X.random --> Y`, then for the corresponding two nodes `x` and `y` in the copied list, `x.random --> y`.

Return *the head of the copied linked list*.

The linked list is represented in the input/output as a list of `n` nodes. Each node is represented as a pair of `[val, random_index]` where:

- `val`: an integer representing `Node.val`
- `random_index`: the index of the node (range from `0` to `n-1`) that the `random` pointer points to, or `null` if it does not point to any node.

Your code will **only** be given the `head` of the original linked list.

Example 1:

![example1](https://assets.leetcode.com/uploads/2019/12/18/e1.png)

```
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
```

Example 2:

![example2](https://assets.leetcode.com/uploads/2019/12/18/e2.png)

```
Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]
```

Example 3:

![example3](https://assets.leetcode.com/uploads/2019/12/18/e3.png)

```
Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]
```

Constraints:

- `0 <= n <= 1000`
- `-10^4 <= Node.val <= 10^4`
- `Node.random` is `null` or is pointing to some node in the linked list.

## Topic
- Hash Table
- Linked List

## My Thinking
雖然此題寫的一大串文字試圖解釋，但其實就一個重點： `把輸入的鏈結串列copy一份，並輸出此copy的鏈結串列`。

只不過此題的鏈結串列內多了一個 `random值`，也因此多了此值，無法直接用一次迴圈遍歷結束就將copy的鏈結串列製作好。

因為此 `random值` 真的如字面上意思是隨機節點，如果在建立 `copy節點` 時剛好此節點的 `random值` 剛好是後面尚未建立的節點的話就會出錯。

因此解題思路：
1. 建立一個 `HashTable` 去紀錄 `只有給定val的copy節點`。其格式為 = `{舊節點: 舊節點對應的copy節點}`。
2. 會需要進行2次迴圈。<br>`第一次迴圈` 是遍歷所有舊節點並只建立 `對應舊節點val值得copy節點(只有val，其餘都尚未設定)`，接著放入 `HashTable` 內。<br>`第二次迴圈` 就是配合先前製作的 `HashTable`，將所有copy的節點剩餘的值賦予值。
3. 這邊要注意一點，因為題目的 `random值` 是有 `null` 值的情形，因此在最初定義 `HashTable` 時，可以先將 `{None: None}` 的 `key/value` 加入。


> 參考影片(思路和他一樣，不過若不知道題目在說什麼可以參考): **By NeetCode**
>
> `Time complexity = O(n), Space complexity = O(n)`
> 
> [![Copy List with Random Pointer - Linked List - Leetcode 138](https://img.youtube.com/vi/5Y2EiZST97Y/hqdefault.jpg)](https://www.youtube.com/watch?v=5Y2EiZST97Y)


### Complexity
Time complexity: O(n)
> 即使遍歷2次在計算 `Time complexity` 時會去掉常數項，因此為 **O(n)**

Space complexity: O(n)
> 因為是用迴圈迭代 `HashTable` 額外空間去儲存 `舊節點的copy節點`，因此為 **O(n)**。