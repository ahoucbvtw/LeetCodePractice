# LeetCode 36 Valid Sudoku
Determine if a `9 x 9` Sudoku board is valid. Only the filled cells need to be validated **according to the following rules**:

1. Each row must contain the digits `1-9` without repetition.
2. Each column must contain the digits `1-9` without repetition.
3. Each of the nine `3 x 3` sub-boxes of the grid must contain the digits `1-9` without repetition.

**Note:**
- A Sudoku board (partially filled) could be valid but is not necessarily solvable.
- Only the filled cells need to be validated according to the mentioned rules.

Example 1:

![example](https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/250px-Sudoku-by-L2G-20050714.svg.png)
```
Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

Output: true
```

Example 2:
```
Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

Output: false

Explanation: 
Same as Example 1, except with the 5 in the top left corner being modified to 8. 
Since there are two 8's in the top left 3x3 sub-box, it is invalid.
```

Constraints:

- `board.length == 9`
- `board[i].length == 9`
- `board[i][j]` is a digit `1-9` or `'.'`.

## Topic
- Array
- Matrix
- Hash Table

## My Thinking
由於要判斷一數獨題目是否真正符合數獨資格是非常複雜，除了題目的3個條件外，還需要判斷 `每個row` 和 `每個col` 的 `交會點` 是否也都符合 `row` 和 `col` 的條件且不互相衝突。

但是題目有額外補充說明2點：
- 判斷現階段已經填好數字的數獨若是 `valid`，也不一定代表此組數獨可以被正確的解出來。
- 只需要判斷目前已經給定的數字是否符合題目給的數獨條件。

根據以上2點，在解題上便可以更簡單的解出此題目，因為只需要檢查目前題目給的數字中是否有符合3個條件，且不需要確認是否真的可以被解出來。

因此解題思路如下：
- 創建3個條件所使用的 `Hash Set`，用來記錄是否有重複值出現。
  - `Hash Set` 是使用 `key-value` 而製作成的 `Hash Table`。<br>ex: {0: ('5', '3', '7'), 1: ('5', '1', '6', '9')}
  - 至於為何使用 `Hash Set` 的原因是可以更方便的紀錄哪一個 `row` 或 `col` 或 `sub-box` 的值。<br>ex: 以 `row` 為例 = {0: ('5', '3', '7'), 1: ('5', '1', '6', '9')}，此時可以看出 `row = 0` 時有 `5,3,7`， `row = 1` 時有 `5,1,6,9`。
  - 當然也可以單純使用 `Set` 就直接達成，只是使用 `Hash Set` 最後可以清楚列出哪一 `row` 或 `col` 有哪些值，方便 debug。
- 按照題目的條件去設置判斷式：
  - 逐一檢查每 `row` 或 `col` 中每個值是否有重複值，並在逐一檢查每 `row` 或 `col` 時，若確定並未在該 `row` 或 `col` 的 `Hash Set` 中的話就加入，以便確認該 `row` 或 `col` 在全部遍歷完後是否還有重複值出現。<br>ex: row=0, ["5","3",".",".","7",".",".",".","."] => 逐一遍歷檢查，若不存在就新增 => `{0: ('5')} -> {0: ('5', '3')} -> {0: ('5', '3', '7')}`。
  - 至於第3個條件則需要做特殊處理。按照下圖，數獨可拆分成9個 `sub-box`，而此 `sub-box` 上的座標系也與原先數獨中的 `row` 與 `col` 息息相關。<br>(0,0)此座標的 `sub-box` 上，可以看到是原先 `row=0-2`, `col=0-2` 所組成。同理(1,2)此座標的 `sub-box` 上，可以看到 `row=3-5`, `col=6-8`。<br>因此可以得知當目前的 `row` 與 `col` 位置去計算 `整除3取商` = 所屬當前 `sub-box` 的座標。<br>ex: `row=3`, `col=8` 的數值會位在 (3//3, 8//3) 的 `sub-box` 內 => (1,2)座標的 `sub-box` 裡面。
  
  ![subbox1](https://github.com/ahoucbvtw/LeetCodePractice/blob/main/LeetCode%20Questions/Medium/36_Valid%20Sudoku/pic/36_1.png?raw=true)

  ![subbox2](https://github.com/ahoucbvtw/LeetCodePractice/blob/main/LeetCode%20Questions/Medium/36_Valid%20Sudoku/pic/36_2.png?raw=true)
  - 在找到第3個條件 `sub-box` 與原先 `9x9` 數獨之間的關係後，便可以與先前2個條件一樣進行逐一遍歷檢查，不存在就新增 => {(0, 0)座標的sub-box: ('6', '9', '5', '8', '3'), (0, 1)座標的sub-box: ('5', '1', '9', '7')} 

> 參考影片: **By NeetCode**
>
> `Time complexity = O(n^2), Space complexity = O(1)`
> 
> [![Valid Sudoku - Amazon Interview Question - Leetcode 36 - Python](https://img.youtube.com/vi/TjFXEUCMqI8/hqdefault.jpg)](https://www.youtube.com/watch?v=TjFXEUCMqI8)


### Complexity
Time complexity: $O(n^2)$
> 雖然在比對數值是否有存在重複時是使用 `x in Set` 的處理方式，此處理方式為 `O(1)`，但由於需要確定每個 `row` 和 `col` 的所值是否符合題目的3個條件而使用連續 `2個for迴圈`，因此為 **$O(n^2)$**

Space complexity: O(1)
> 由於不管是在判斷是否在Set內或是Set的增刪都是 `直接取得Matrix(2為陣列)中指定位置值`，因此為 **O(1)**