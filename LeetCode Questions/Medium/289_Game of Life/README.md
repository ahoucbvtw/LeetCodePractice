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