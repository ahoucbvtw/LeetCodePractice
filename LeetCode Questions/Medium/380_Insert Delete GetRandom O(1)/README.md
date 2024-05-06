# LeetCode 380 Insert Delete GetRandom O(1)

Implement the `RandomizedSet` class:

- `RandomizedSet()` Initializes the `RandomizedSet` object.
- `bool insert(int val)` Inserts an item `val` into the set if not present. Returns `true` if the item was not present, `false` otherwise.
- `bool remove(int val)` Removes an item `val` from the set if present. Returns `true` if the item was present, `false` otherwise.
- `int getRandom()` Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the **same probability** of being returned.

You must implement the functions of the class such that each function works in **average** `O(1)` time complexity.

Example 1:
```
Input
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output
[null, true, false, true, 2, true, false, 2]

Explanation
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2); // 2 was already in the set, so return false.
randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.
```

Constraints:

- `-2^31 <= val <= 2^31 - 1`
- At most `2 * 10^5` calls will be made to `insert`, `remove`, and `getRandom`.
- There will be **at least one element** in the data structure when `getRandom` is called.

## Topic
- Array
- Math
- Design
- Hash Table
- Randomized

## My Thinking
此題出的非常的好，因為它要求製作 `class` 並且裡面所有 function 的 `Average Time complexity = O(1)`。<br>由於題目限制，因此在進行新增與刪除時必須要避免造成 `O(n)`。

---
首先必須要先了解各資料結構新增與刪除的特性:

**List**

| Description |    Method    |  Average Time complexity  |
|:-----------:|:------------:|:-------------------------:|
|    Search   |    List[0]   |            **O(1)**           |
|    Exist    |   x in List  |            O(n)           |
|     Add     | List.append()|            **O(1)**           |
|   Delete(last value)   |  List.pop(), List.remove(last value), del List[-1] |            **O(1)**           |
|   Delete(not last value)   |  List.pop(1), List.remove(not last value), del List[0] |            O(n)           |

---

**Set**

| Description |    Method    |  Average Time complexity  |
|:-----------:|:------------:|:-------------------------:|
|    Exist    |   x in Set   |            **O(1)**           |
|     Add     | Set.add()    |            **O(1)**           |
|   Delete   |  Set.pop(), Set.remove(value) |            **O(1)**           |

---

**HashTable**

| Description |    Method    |  Average Time complexity  |
|:-----------:|:------------:|:-------------------------:|
|    Exist    |   x in HashTable   |            **O(1)**           |
|     Add     | HashTable[value]    |            **O(1)**           |
|   Delete   |  HashTable.remove(value) |        **O(1)**           |

---

在了解上面這些特性後，就可以判斷要用何種方式達成題目要求每個function 的 `Average Time complexity` 在 `O(1)` 的條件。

> 參考資料:
>
> - [Time complexity of python set operations?](https://stackoverflow.com/questions/7351459/time-complexity-of-python-set-operations)
> 
> - [【Python】List V.S Set 時間複雜度比較 Time Complexity](https://missterhao.me/2019/02/01/%E3%80%90python%E3%80%91list-v-s-set-%E6%99%82%E9%96%93%E8%A4%87%E9%9B%9C%E5%BA%A6%E6%AF%94%E8%BC%83-time-complexity/)
>
> - [Python Wiki TimeComplexity](https://wiki.python.org/moin/TimeComplexity)
>
> - [What is the time complexity of random.choice in python and how does it actually work?](https://stackoverflow.com/questions/73044555/what-is-the-time-complexity-of-random-choice-in-python-and-how-does-it-actually)
>
> - [Big-O complexity of random.choice(list) in Python3](https://stackoverflow.com/questions/40143157/big-o-complexity-of-random-choicelist-in-python3)

<br><br>由於新增與刪除，直覺會想到使用 `Array`，但 `Array`的刪除如上所示有限制必須是最後一個值才會是 `O(1)`，否則都會是 `O(n)`。

而若是改用 `Set` 似乎可以避免掉此麻煩，但因為還需要考慮到題目的第3個function要求: `隨機列出一個值，且每個值出現機率皆相同`。<br>在 `隨機` 上各程式語言都已經有現成的工具可以使用，因此不需要自己手刻。Python而言就是 `random` 套件<br>要達成題目要求最快方式是使用 `random.choice()`，只是此方法只適用在 `Array`，沒法用在 `Set`。<br>且 `Set` 和 `HashTable` 若是要轉換成 `Array` `( list(Set) / list(HashTable.keys()) )` 就會是 `O(n)` 而不是 `O(1)`，不符合題目要求。

因此在新增與刪除數值方面就只能考慮使用 `Array`。不過這樣也有問題，若是當題目刪除的並非最後一個該如何讓它變成 `O(1)` ?

很簡單，利用 `HashTable` 來紀錄新增數值是位在 `Array` 哪個 index 上即可。<br>**刪除時只要配合 `HashTable` 就可以輕鬆將要刪除的值與最後一個值互相對調，再使用 `pop()` 即可達成 `O(1)`效果。**

並且 `HashTable` 也可以通過 `val in HashTable` 方式查看是否已經有數字存在。<br>至於為什麼不使用 `val in Array` 而是用 `val in HashTable` 檢查原因如上方表格呈現，若是使用 `val in Array` 會造成 `O(n)`，但是 `val in HashTable` 則是 `O(1)`。

結論:<br>因為受限題目需要 `O(1)` 的要求，使用 `Array` 紀錄新增與刪除的數字以及使用 `HashTable` 紀錄那些數字在 `Array` 的 index，兩者互相配合即可達成3個 function 的 `Average Time complexity` 在 `O(1)` 的條件。

### Complexity
Time complexity: O(1)
> 從頭到尾不管是使用 `val in HashTable` 或是刪除時先將該值對調至 `Array` 最後方再 `pop()`，都按照題目要求，因此為**O(1)**

Space complexity: O(n)
> 因為此題目需要製作一個 `HashTable`，若是準備新增的數字有 `n個`，那新增的動作就會做 `n遍`，因此為**O(n)**