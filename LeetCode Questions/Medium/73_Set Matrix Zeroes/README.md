# LeetCode 73 Set Matrix Zeroes
Given an `m x n` integer matrix `matrix`, if an element is `0`, set its entire row and column to `0`'s.

You must do it **in place**.

Example 1:

![Example1](https://assets.leetcode.com/uploads/2020/08/17/mat1.jpg)

```
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
```

Example 2:

![Example2](https://assets.leetcode.com/uploads/2020/08/17/mat2.jpg)

```
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
```

Constraints:

- `m == matrix.length`
- `n == matrix[0].length`
- `1 <= m, n <= 200`
- `-2^31 <= matrix[i][j] <= 2^31 - 1`

Follow up:

- A straightforward solution using `O(mn)` space is probably a bad idea.
- A simple improvement uses `O(m + n)` space, but still not the best solution.
- Could you devise a constant space solution?

## Topic
- Array
- Matrix
- Hash Table

## My Thinking
由於看了 **NeetCode** 的 `Space O(1)` 解題思路還是不知道該如何撰寫，因此改用最一目了然也是題目有提到的 `Space O(m+n)`。

由於題目要求若有0出現其行與列都要跟著改成0，且不能額外輸出一個矩陣，只能用原陣列更改。<br>因此不管再怎麼設計，`Time = O(mn)`，因為會需要遍歷所有矩陣，才能知道哪裡有0。

因此 `Space O(m+n)` 的解題思路為：
- 建立與矩陣行與列2個相同長度的陣列。<br>一個紀錄該矩陣中哪一列有0，另一個紀錄該矩陣中哪一行有0。
- 遍歷第一次矩陣找出0的位置，並將該行與該列的位置紀錄在2個陣列中。
- 利用紀錄完畢的2個陣列，再次進行矩陣遍歷，並且遇到紀錄的 `行或列 = True`，則將該矩陣位置的值改為0。

![Space O(m+n)1](https://github.com/ahoucbvtw/LeetCodePractice/blob/main/LeetCode%20Questions/Medium/73_Set%20Matrix%20Zeroes/pic/1.PNG?raw=true)

![Space O(m+n)2](https://github.com/ahoucbvtw/LeetCodePractice/blob/main/LeetCode%20Questions/Medium/73_Set%20Matrix%20Zeroes/pic/2.png?raw=true)

> 參考影片: **By NeetCode**
>
> `Time complexity = O(mn), Space complexity(Best) = O(1)`
> 
> [![Set Matrix Zeroes - In-place - Leetcode 73](https://img.youtube.com/vi/T41rL0L3Pnw/hqdefault.jpg)](https://www.youtube.com/watch?v=T41rL0L3Pnw)


### Complexity
Time complexity: O(mn)
> 因為不管如何都會需要針對矩陣全部遍歷一次，因此為 **O(mn)**

Space complexity: O(m+n)
> 因為額外使用 `2個陣列紀錄哪個行與列 = 0`，因此為 **O(m+n)**。