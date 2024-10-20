# LeetCode 637 Average of Levels in Binary Tree
Given the `root` of a binary tree, *return the average value of the nodes on each level in the form of an array.* Answers within `10^-5` of the actual answer will be accepted.


Example 1:

![example1](https://assets.leetcode.com/uploads/2021/03/09/avg1-tree.jpg)

```
Input: root = [3,9,20,null,null,15,7]
Output: [3.00000,14.50000,11.00000]
Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
Hence return [3, 14.5, 11].
```

Example 2:

![example1](https://assets.leetcode.com/uploads/2021/03/09/avg2-tree.jpg)

```
Input: root = [3,9,20,15,7]
Output: [3.00000,14.50000,11.00000]
```

Constraints:

- The number of nodes in the tree is in the range `[1, 10^4]`.
- `-2^31 <= Node.val <= 2^31 - 1`

## Topic
- Tree
- Binary Tree
- Depth-First Search
- Breadth-First Search

## My Thinking
此題目給定一根節點的二元樹，它需要我們計算此 **二元樹每一層(Level)節點值的平均** ，並輸出至一陣列中。

因為題目需要 **計算樹的每一層(Level)** 節點值的平均，因此我選用 **BFS(Breadth-First Search)** 演算法來實踐。

至於為什麼會選擇此演算法那是因為此演算法的搜尋特性

它的搜尋方式是像雷達一樣一層一層暴力的遍歷搜尋，如下圖：

![BFS](https://upload.wikimedia.org/wikipedia/commons/4/46/Animated_BFS.gif)
引用：https://en.wikipedia.org/wiki/Breadth-first_search

而剛好此搜尋的特性與題目所需要的 **計算樹每一層(Level)** 節點值平均非常符合，因此本題使用此演算法進行解題。<br><br>

過程中與一般BFS演算法寫法相同，不一樣的地方在於需要將每一層節點值抓出來再平均。

因此在每次判斷 Queue 是否為空的時候都需要進行 Queue 長度的計算

再使用此計算 **搭配for迴圈加速BFS對每一層(Level)** 的進行。<br><br>

這樣就可以針對每一層(Level)節點值平均的計算。


### Complexity
Time complexity: O(n)
> 雖然在BFS中使用for迴圈，但是此迴圈只是單純加速BFS的進程，也就是將每次判斷 Queue 是否為空的時機點 **變更成每一層(Level)運算結束** ，因此不引響還是維持 **O(n)**

Space complexity: O(n)
> 因為在使用BFS演算法的同時會預先創建一個 Queue 幫助運算，而 Queue 也算是 Array 資料結構的一種，因此為 **O(n)**。