# LeetCode 61 Rotate List
Given the `head` of a linked list, rotate the list to the right by `k` places.

Example 1:

![example1](https://assets.leetcode.com/uploads/2020/11/13/rotate1.jpg)

```
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
```

Example 2:

![example2](https://assets.leetcode.com/uploads/2020/11/13/roate2.jpg)

```
Input: head = [0,1,2], k = 4
Output: [2,0,1]
```

Constraints:

- The number of nodes in the list is in the range [`0, 500]`.
- `-100 <= Node.val <= 100`
- `0 <= k <= 2 * 10^9`

## Topic
- Linked List
- Two Pointers

## My Thinking
此題與 [189_Rotate Array](https://github.com/ahoucbvtw/LeetCodePractice/tree/main/LeetCode%20Questions/Medium/189_Rotate%20Array) 一樣，不過這次是 `Linked List`，因此無法使用與 **189** 一樣的解法。

解題思路：
1. 因為是 `Linked List` 沒辦法使用函式得知其長度，因此首先必須要先找出此 `Linked List` 的長度，並且將最後的節點給標註(tail)。
2. 得到 `Linked List` 的長度以後就可以根據題目給的k去判斷是否需要 `Rotate ? 輪迴`，`k % Linked List長度(取餘數)`。<br>若 `餘數 = 0` 則表示剛剛好輪迴成原先一樣的位置。<br>若 `餘數 ≠ 0` 則表示有變化。
3. 當判定 `餘數 ≠ 0` 時，就要從頭開始移動至 `Linked List長度 - 餘數 - 1` 的位置(斷開節點的前一個節點)，將鏈結斷開<br>。並將下一個節點以後的所有節點並移動至開頭。<br>而此時原先最後的標註節點(tail)就會剛好是被斷開節點群的最後一個，因此他必須要鏈結原先的 `head` 這樣才算完成 `k` 次的 `Rotate`。

> 參考影片: **By NeetCode**
>
> `Time complexity = O(n), Space complexity = O(1)`
> 
> [![Rotate List - Linked List - Leetcode 61 - Python](https://img.youtube.com/vi/UcGtPs2LE_c/hqdefault.jpg)](https://www.youtube.com/watch?v=UcGtPs2LE_c)


### Complexity
Time complexity: O(n)
> 因為使用迴圈進行遍歷全部鏈結串列，因此為 **O(n)**

Space complexity: O(1)
> 因為在解題的過程中並未需要迭代的額外空間進行儲存，因此為 **O(1)**。