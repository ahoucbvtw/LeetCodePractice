# LeetCode 452 Minimum Number of Arrows to Burst Balloons
There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array `points` where `points[i] = [x_start, x_end]` denotes a balloon whose **horizontal diameter** stretches between `x_start` and `x_end`. You do not know the exact y-coordinates of the balloons.

Arrows can be shot up **directly vertically** (in the positive y-direction) from different points along the x-axis. A balloon with `x_start` and `x_end` is burst by an arrow shot at `x` if `x_start <= x <= x_end`. There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

Given the array `points`, return *the minimum number of arrows that must be shot to burst all balloons*.

Example 1:
```
Input: points = [[10,16],[2,8],[1,6],[7,12]]
Output: 2
Explanation: The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
- Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].
```

Example 2:
```
Input: points = [[1,2],[3,4],[5,6],[7,8]]
Output: 4
Explanation: One arrow needs to be shot for each balloon for a total of 4 arrows.
```

Example 3:
```
Input: points = [[1,2],[2,3],[3,4],[4,5]]
Output: 2
Explanation: The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 2, bursting the balloons [1,2] and [2,3].
- Shoot an arrow at x = 4, bursting the balloons [3,4] and [4,5].
```

Constraints:

- `1 <= points.length <= 10^5`
- `points[i].length == 2`
- `-2^31 <= x_start < x_end <= 2^31 - 1`

## Topic
- Array
- Greedy
- Sorting

## My Thinking
由於此題目並未說明該氣球是否有按照區間大小做排序，因此一率先進行排序。<br>而只要進行排序，`Time complexity = O(nlogn)`。

參考 **NeetCode** 的影片可以得出下面的解題思路：
- 因為要找尋可以用最少箭矢讓氣球爆炸，因此就必須找到放在x軸座標上直徑有重疊的氣球，且必須是找到所有重疊氣球的x軸重疊範圍。
  - 而在找尋重疊氣球的重疊範圍時，必須要一直找下去直到下一個氣球並沒有與前面所有氣球的重疊範圍重疊。<br>ex: [[1,6],[2,8],[5,10],[11,12]] => 這4顆氣球的重疊範圍就是依序 => [1,6],[2,8] 比對 -> 重疊範圍[2,6] => 上一個重疊範圍[2,6],[5,10] 比對 -> 新重疊範圍[5,6] => 上一個重疊範圍[5,6],[11,12] 比對 -> 兩者並沒有重疊。
- 每找到一個重疊範圍時就用 `最多的箭矢方法 - 1`。

> 參考影片: **By NeetCode**
>
> `Time complexity = O(nlogn), Space complexity = O(n)`
> 
> [![Minimum Number of Arrows to Burst Balloons - Leetcode 452 - Python](https://img.youtube.com/vi/lPmkKnvNPrw/hqdefault.jpg)](https://www.youtube.com/watch?v=lPmkKnvNPrw)


### Complexity
Time complexity: $O(nlogn)$
> 即時用迴圈遍歷是 `O(n)`，但因為已經先進行 `sort()`，因此為 **$O(nlogn)$**

Space complexity: O(n)
> 因為在確認是否有多個氣球重疊時，就已經一直迭代儲存新的重疊範圍，因此為 **O(n)**。