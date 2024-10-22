# LeetCode 112 Path Sum
Given the `root` of a binary tree and an integer `targetSum`, return `true` if the tree has a **root-to-leaf** path such that adding up all the values along the path equals `targetSum`.


Example 1:

![example1](https://assets.leetcode.com/uploads/2021/01/18/pathsum1.jpg)

```
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.
```

Example 2:

![example2](https://assets.leetcode.com/uploads/2021/01/18/pathsum2.jpg)

```
Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There are two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.
```

Example 3:

```
Input: root = [], targetSum = 0
Output: false
Explanation: Since the tree is empty, there are no root-to-leaf paths.
```

Constraints:

- The number of nodes in the tree is in the range `[0, 5000]`.
- `-1000 <= Node.val <= 1000`
- `-1000 <= targetSum <= 1000`

## Topic
- Tree
- Binary Tree
- Depth-First Search
- Breadth-First Search

## My Thinking
此題目給定一根節點的二元樹，它需要我們判斷按照 **從根的數值一路向下相加到樹葉** 的數值是否等於給定的 `targetSum` 。

因為題目是要求 **從根開始到葉子** 相加判斷，因此可以使用 **DFS演算法(Depth-First Search)** 進行撰寫。

至於為什麼會選擇此演算法那是因為此演算法的搜尋特性就是 **從根開始往其中一個分支去搜尋直到盡頭為止**，如下圖：

![DFS](https://upload.wikimedia.org/wikipedia/commons/thumb/7/7f/Depth-First-Search.gif/440px-Depth-First-Search.gif)
引用：https://en.wikipedia.org/wiki/Depth-first_search

而剛好此搜尋的特性與題目所需要的 **從根開始到葉子** 條件相符合。<br><br>

過程中與一般DFS演算法寫法相同，不一樣的地方在於我們需要判斷何時目前遍歷的節點是否為 `葉子節點(Leaf Node)`。

以及將每次遍歷的節點值做相加直到葉子節點時再判斷 `目前相加值是否 = targetSum`。


### Complexity
Time complexity: O(n)
> 在DFS中因為需要訪問每個節點一次，因此為 **O(n)**

Space complexity: O(n)
> 在DFS中因為要使用遞迴手法遍歷節點， **遞迴的次數在於欲遍歷樹的高度** ，所以嚴格上來說應該為 **O(H)** (H: 樹的高度)， **但是當樹的高度越高，也等同於有N層** ，因此統一表示為 **O(n)**。