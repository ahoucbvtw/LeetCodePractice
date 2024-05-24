# LeetCode 289 Game of Life
According to [Wikipedia's article](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life): "**The Game of Life**, also known simply as **Life**, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an `m x n` grid of cells, where each cell has an initial state: live (represented by a `1`) or dead (represented by a `0`). Each cell interacts with its [eight neighbors](https://en.wikipedia.org/wiki/Moore_neighborhood) (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

1. Any live cell with fewer than two live neighbors dies as if caused by under-population.
2. Any live cell with two or three live neighbors lives on to the next generation.
3. Any live cell with more than three live neighbors dies, as if by over-population.
4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the `m x n` grid `board`, return the next state.

Example 1:

![Example1](https://assets.leetcode.com/uploads/2020/12/26/grid1.jpg)

```
Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
```

Example 2:

![Example2](https://assets.leetcode.com/uploads/2020/12/26/grid2.jpg)

```
Input: board = [[1,1],[1,0]]
Output: [[1,1],[1,1]]
```

Constraints:

- `m == board.length`
- `n == board[i].length`
- `1 <= m, n <= 25`
- `board[i][j]` is `0` or `1`.

Follow up:

- Could you solve it in-place? Remember that the board needs to be updated simultaneously: You cannot update some cells first and then use their updated values to update other cells.
- In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches upon the border of the array (i.e., live cells reach the border). How would you address these problems?

## Topic
- Array
- Matrix
- Simulation

## My Thinking
此題有一個重點：必須要直接更改 `Input Matrix`，不能額外輸出一個新的 `Matrix`。

而由於必須要直接更改，因此需要額外手段才能在更動數值後，還能知道原先值的相關性(題目只求目前盤面的下一輪每格是 `死 = 0` 還是 `活 = 1` )。

1. 使用額外空間去紀錄當下該格子下一輪的生死，不動原先的 `Matrix`。<br>因為如果先更改原先的 `Matrix` 後，後面的格子會因為遊戲規格的關係會有需要判斷先前已經判斷完畢的值，此時就會變得非常混亂。<br>因為不管是生還是死都會有4種結果：<br>`生 -> 生` / `生 -> 死` / `死 -> 死` / `死 -> 生`。<br><br>若是所有判斷完畢的該格子都是 `生 -> 死` 或 `死 -> 生` 這2種還比較好操作，但今天按照遊戲規則判斷下來便會有4種結果，因此就不能動原先 `Matrix`，好讓後續格子也能正常按照規則判斷下一輪的生死。
2. 使用一個虛擬的 `對照表` 如下，不使用額外空間儲存改變的下一輪值，直接按照 `對照表的可能性` 去更改其 `狀態值`。<br>以對照表1為例，若原先該格子是活(1)，但是經過遊戲規則判定下一輪是死(0)，則將該格子更改為 `狀態值1`。<br><br>至於為什麼是使用 `對照表1`？<br>這是因為剛剛的範例就算他的狀態值被改成1，也還是可以直覺的判斷出該格子原先是活(1)。<br>如果換作是 `對照表2`，若原先該格子是死(0)，但是經過遊戲規則判定下一輪是活(1)，則將該格子更改為 `狀態值1`。<br>因為遊戲規則的緣故，後面正在判斷的格子也會需要前面已經判斷過的原先值進行判斷，但是此時該狀態值又是1，會與活(1)做搞混，因此使用 `對照表1` 較為合適。

2者比較後，會是 `方法2` 較為優秀。<br>因為並沒有使用到額外的空間，只有憑空想像一個虛擬對照表。<br>並且按照此對照表不僅可以得知原先的值(生1或死0)也可以得知下一輪的生死，而不影響後面格子進行遊戲規則的判斷。

```python
對照表1(完美)
    原本     下一輪    狀態值
#  0(死)     0(死)      0
#  1(生)     0(死)      1
#  0(死)     1(生)      2
#  1(生)     1(生)      3

對照表2(糟糕)
    原本     下一輪    狀態值
#  0(死)     0(死)      0
#  0(死)     1(生)      1
#  1(生)     0(死)      2
#  1(生)     1(生)      3
```

至於題目列的4項遊戲規則，可以總結出2項結果：
1. 原先活(1): 
  - 如果該格子4周8方位有剛好 `2個 or 3個` 是活(1)，此格子下一輪也會是活(1)。
  
  ![活(1) -> 活(1)](https://github.com/ahoucbvtw/LeetCodePractice/blob/main/LeetCode%20Questions/Medium/289_Game%20of%20Life/pic/1.png?raw=true)
  - 除了上面條件以外，此格子下一輪都是死(0)。
  
  ![活(1) -> 死(0)](https://github.com/ahoucbvtw/LeetCodePractice/blob/main/LeetCode%20Questions/Medium/289_Game%20of%20Life/pic/2.png?raw=true)
1. 原先死(0):
  - 如果該格子4周8方位有 `3個` 是活(1)，此格子下一輪便會是活(1)。
  
  ![死(0) -> 活(1)](https://github.com/ahoucbvtw/LeetCodePractice/blob/main/LeetCode%20Questions/Medium/289_Game%20of%20Life/pic/3.png?raw=true)
  - 除了上面條件以外，此格子下一輪都還是死(0)。
  
  ![死(0) -> 死(0)](https://github.com/ahoucbvtw/LeetCodePractice/blob/main/LeetCode%20Questions/Medium/289_Game%20of%20Life/pic/4.png?raw=true)

> 參考影片: **By NeetCode**
>
> `Time complexity = O(mn), Space complexity = O(1)`
> 
> [![Game of Life - Leetcode 289 - Python](https://img.youtube.com/vi/fei4bJQdBUQ/hqdefault.jpg)](https://www.youtube.com/watch?v=fei4bJQdBUQ)


### Complexity
Time complexity: O(mn)
> 因為需要針對矩陣全部遍歷一次才能知道原先哪個是存活哪個是非存活，才能按照遊戲規則進行新一輪判定，因此為 **O(mn)**

Space complexity: O(1)
> 因為在進行存活和非存活轉換前，`使用的虛擬自定義不存在的對照表，並且按照此對照表進行針對每個值做對照表的狀態轉換`，並未額外使用任何儲存空間，因此為 **O(1)**。