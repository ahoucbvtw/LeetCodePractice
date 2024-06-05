# LeetCode 2 Add Two Numbers
You are given two **non-empty** linked lists representing two non-negative integers. The digits are stored in **reverse order**, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:

![example1](https://assets.leetcode.com/uploads/2020/10/02/addtwonumber1.jpg)

```
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
```

Example 2:
```
Input: l1 = [0], l2 = [0]
Output: [0]
```

Example 3:
```
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
```

Constraints:

- The number of nodes in each linked list is in the range `[1, 100]`.
- `0 <= Node.val <= 9`
- It is guaranteed that the list represents a number that does not have leading zeros.

## Topic
- Math
- Recursion
- Linked List

## My Thinking
題目說要將2個鏈結串列值取出反轉後相加，然後再按照反轉的方式放置新的鏈結串列中。

原先看到題目就慌了，但是仔細觀察一下給的 `example` 可以發現其實跟不需要理會翻轉。<br>因為所有鏈結串列的開頭節點都會是數值的個位數值開始，再來下一個是十位數依此類推。

所以只需要專注在每一個節點的相加即可，不需要在意翻轉。

因此題目的解題思路：
1. 設置一空的虛擬節點當作解答的鏈結串列開頭。
2. 考慮到題目並未明說提供的2個鏈結串列長度是否一樣，因此在撰寫上 `必須考慮到2者長度不一的情況`。
   1. 當2者長度不一樣的時候，一定會有一方先被遍歷完畢。<br>因此就必須要 `將長度較短那方後面的節點值持續補0，直到較長的一方全部遍歷完畢。`
3. `在進行相加的時候，必須要考慮到進位的問題。`<br>將相加後的個位數帶入新節點，並將進位的數值傳遞給下一位數的數值相加上。
4. 最後還需要考慮的就是若 `當遍歷到最後一個節點時，此時相加也需要進位的情況。`<br>因為若不考慮此情況此鏈結串列就會在最後面少一個位數的節點值。

> 參考影片(思路和他一樣，不過簡化寫法可以參考): **By NeetCode**
>
> `Time complexity = O(n), Space complexity = O(1)`
> 
> [![Add Two Numbers - Leetcode 2 - Python](https://img.youtube.com/vi/wgFPrzTjm7s/hqdefault.jpg)](https://www.youtube.com/watch?v=wgFPrzTjm7s)

### Complexity
Time complexity: O(n)
> 因為在進行2個鏈結串列數值相加時是遍歷較長的一方，因此為 **O(n)**

Space complexity: O(1)
> 就算額外使用空間去紀錄新的空鏈結串列的節點，在題目的操作上也只是去操作他的next值，並不會因此而儲存到 `O(n)` 的空間，因此為 **O(1)**。