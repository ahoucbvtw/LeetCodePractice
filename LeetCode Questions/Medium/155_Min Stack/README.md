# LeetCode 155 Min Stack
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the `MinStack` class:
- `MinStack()` initializes the stack object.
- `void push(int val)` pushes the element `val` onto the stack.
- `void pop()` removes the element on the top of the stack.
- `int top()` gets the top element of the stack.
- `int getMin()` retrieves the minimum element in the stack.

You must implement a solution with `O(1)` time complexity for each function.

Example 1:
```
Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
```

Constraints:

- `-2^31 <= val <= 2^31 - 1`
- Methods `pop`, `top` and `getMin` operations will always be called on **non-empty** stacks.
- At most `3 * 10^4` calls will be made to `push`, `pop`, `top`, and `getMin`.


## Topic
- Stack
- Design

## My Thinking
在準備寫此題之前必須先瞭解 `Stack` 是什麼東西。

`Stack` 是一種陣列的資料結構，由下往上進行堆疊。<br>與 `Queue` 相反，`Stack` 的任何動作都必須從 `top` 進行，因此有 `先進後出` 特性 `Last In First Out => LIFO`。

在 `Stack` 資料結構的新增、刪除 => `push`、`pop`。<br>如同上面所說它有 `先進後出` 的特性，因此在做 `push`、`pop` 時也都是操作最後的值。

> ![Stack push & pop](https://ithelp.ithome.com.tw/upload/images/20210916/20121027edOmUwqfoe.jpg)
> From [【Day5】[資料結構]-堆疊Stack](https://ithelp.ithome.com.tw/articles/10265265)

---

此題目要求製作一個 `MinStack` Class，裡面會需要有 `push`、`pop`、`top`、`getMin` 4個函式，且必須要在 `Time complexity = O(1)` 完成。

而這4個函式分別代表：
- `push` : 將值放進 `Stack` 中。
- `pop` : 將 `Stack` 中的 `top` 值取出。
- `top` : 取得 `Stack` 中的 `top` 值。
- `getMin` : 取得 `Stack` 中的 `最小值`。

此4個函式中前3個較為簡單，且也都是 `Stack` 資料結構的特性。<br>但是第4個函式 `getMin` 就稍微麻煩，因為題目有限制 `Time complexity = O(1)`，因此不能使用每次呼叫此函式時進行陣列遍歷尋找最小值，會變成 `O(n)`。

不過在撰寫 `getMin` 函式時，也可以套用 `Stack` 的資料結構。
- 首先建立2個 `Stack` 陣列，一個用來儲存第1~3的所有函式操作; 另一個則是用來儲存陣列中最小值。
- 每當有數值因為使用 `push` 函式放進第一個 `Stack` 陣列時，就去比較上一個值與此次的值哪個較小，並將較小的值放入最小值的 `Stack` 陣列。
- 每當有數值因為使用 `pop` 函式從 `top` 被移除時，最小值的 `Stack` 陣列也需要一起移除位於陣列中的 `top` 值。
  - 最小值的 `Stack` 陣列其每一個值所代表的含義是當下那個回合的最小值。<br>因此就算移除 `top` 值，也只是移除剛剛使用 `push` 函式放入的值做比較的最小值回合，並不會影響到先前每一回合的最小值。
- 由於使用最小值的 `Stack` 陣列紀錄每一回合的最小值，因此按照 `Stack` 資料結構的特性，該陣列的最後一個加入的值就會是最小值。<br>且剛好題目也有額外說明 `pop`、`top`、`getMin` 這3個函式不會在 `Stack` 陣列是空的時候呼叫，因此可以放心將最小值的 `Stack` 陣列的最後一個值輸出為答案。

### Complexity
Time complexity: O(1)
> 因為題目要求在製作 `getMin` 函式時並未使用迴圈遍歷，而是使用每次在 `push` 時比較先前 `最小Stack陣列` 的 `top值`，將新的較小的值寫入此陣列中，因此為 **O(1)**

Space complexity: O(n)
> 因為在 `getMin` 函式以及其他函式也共使用2個 `Stack` 陣列去紀錄，因此為 **O(n)**。