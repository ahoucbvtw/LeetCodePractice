# LeetCode 92 Reverse Linked List II
Given the `head` of a singly linked `list` and two integers `left` and `right` where `left <= right`, reverse the nodes of the list from position `left` to position `right`, and return the reversed list.

Example 1:

![example1](https://assets.leetcode.com/uploads/2021/02/19/rev2ex2.jpg)

```
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
```

Example 2:
```
Input: head = [5], left = 1, right = 1
Output: [5]
```

Constraints:

- The number of nodes in the list is `n`.
- `1 <= n <= 500`
- `-500 <= Node.val <= 500`
- `1 <= left <= right <= n`

Follow up: Could you do it in one pass?

## Topic
- Linked List

## My Thinking
此題我原先認為只是單純的將 `Linked List` 的指定位置的 `left` 和 `right` 兩個節點互換而已。<br>結果實際提交後才發現是除了兩個節點互換外，還要將 `left` 和 `right` 兩個節點內的所有節點給反向連結。

我原先是在考慮額外搭配 `HashTable` 使用，以 `Linked List` 連接的順序為key，單純節點值為value，來達成。不過後來想想如果這樣做的話 `Space complexity = O(n)`，所以就參考**Nikhil Lohia**影片來達到 `Space complexity = O(1)` 的寫法。

此題的解題思維：
1. 建立一個 `虛擬的節點(dummy)` 當作頭，並且設定 `Lpre` 用來記錄left的前一個節點，並且 `Lpre` 是從 `虛擬的節點(dummy)` 開始移懂，`cur` 則是原先的 `head` 開始移動到 `left節點`，此時只會移動 `left - 1` 的步數。
2. 因為上一步已經找到題目的 `left節點`，因此接下來直到找到 `rgiht節點` 前，都是需要將原先的節點進行反向鏈結。
   1. 先設置 `pre` 紀錄 `cur` 的前一個節點，並且將該節點指定為 `None`。
   2. 經過上一步驟，此時 `cur` 會在 `left節點` 上。<br>並且 `pre` 和 `cur` 繼續移動直到 `cur` 抵達 `rgiht節點` 的下一個位置，此時移動量就會是 `right - left + 1` 的步數。<br>目的就是要將 `pre` 鎖定在 `right位置`，`cur` 鎖定在 `right位置` 下一個位置。
   3. 另外在移動 `pre` 和 `cur` 的過程還需要順便將沿路經過的 `節點next` 給反向鏈結。<br>不過在反向鏈結前需要先製作一個變數去儲存原先的鏈結的下一個節點，否則如果先斷開後，就無法繼續按照原先 `Linked List` 向前遍歷。
3. 在經過第2步後，`left` 和 `right` 內的所有節點都已經被反向鏈結，因此只會剩下交換 `left` 和 `right` 位置。
   1. 交換時其實只需要操作原先 `Lpre節點` 和原先的 `left節點`。
   2. 因為在交換後，原先的 `left節點` 就會 = `Lpre.next`，因此在原先的 `left節點` 交換到 `rgiht節點` 後，其下一個節點就會是上一步中 `cur` 的位置。
   3. 而因為 `left` 和 `right` 交換後，`Lpre節點` 下一個新的節點就會是上一步驟中的 `pre` 位置。

> 參考影片(解釋較清晰): **By Nikhil Lohia**
>
> `Time complexity = O(n), Space complexity = O(1)`
> 
> [![Reverse Linked List 2 (LeetCode 92) | Full simplified solution | Animations and Demo](https://img.youtube.com/vi/oDL8vuu2Q0E/hqdefault.jpg)](https://www.youtube.com/watch?v=oDL8vuu2Q0E)


### Complexity
Time complexity: O(n)
> 因為使用迴圈進行遍歷，因此為 **O(n)**

Space complexity: O(1)
> 因為在解題的過程中並未需要迭代的額外空間進行儲存，因此為 **O(1)**。