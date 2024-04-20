# LeetCode 189 Rotate Array
Given an integer array `nums`, rotate the array to the right by `k` steps, where `k` is non-negative.

Example 1:
```
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
```

Example 2:
```
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
```

Constraints:

- `1 <= nums.length <= 10^5`
- `-2^31 <= nums[i] <= 2^31 - 1`
- `0 <= k <= 10^5`

## Topic
- Array
- Math
- Two Pointers

## My Thinking
題目給定執行k次，每次執行的時候會把陣列最後一項移動到第一項，找出執行k次後陣列的值會變成什麼樣子
```
k=2, nums=[1,2,3,4,5]
第1次: nums=[5,1,2,3,4]
第2次: nums=[4,5,1,2,3]
```

上面範例中 `k=2, nums=[1,2,3,4,5]` 最後會變成 `nums=[4,5,1,2,3]`

從中發現可以看成這樣 `X|Y` -> `Y|X`，也就是進行反轉，但是若將 `X=123, Y=45` 做反轉的話 -> `54|321`

再將剛剛經過反轉的 `Y|X = 54|321` 與答案做比較 `45123` 可以發現答案也可以被拆分為 `45|123`

而若是再一次將 `X`,`Y` 各別做反轉 `X'`,`Y'` 就與答案相同

`Y|X = 54|321` -> `Y'|X' = 45|123`

而此時解題思路就是：
1. 先將原先陣列進行反轉
2. 將反轉後的陣列按照 `陣列k的位置處` 前後各別再進行反轉
3. 注意事項：如果 `k > 原先陣列長度` 表示一直往前搬運過程已經經過一輪，正在進行第2,3...輪

因此在進行反轉前，必須要先知道真正的k是多少

從下面的範例可以得知 `k=7, 陣列長度=3`，但實際最後答案卻會等於 `k=2` 的結果

因此 `得知真正k的方法 = k/陣列長度，然後取餘數`

```
ex: k=7, [1,2,3]
1: [3,1,2]
2: [2,3,1]
3: [1,2,3] => 第一輪，與原陣列相同
4: [3,1,2] => 與第一次相同
5: [2,3,1] => 與第二次相同
6: [1,2,3] => 第二輪，與原陣列相同
7: [3,1,2] => 與第一次相同
```

### Complexity
Time complexity: O(n)
> 因為進行陣列反轉，將陣列中每個數字重新進行鏡像排列，所以是 **O(n)**

Space complexity: O(1)
> 每一次更改呼叫陣列時都是使用指定區間的方式 `nums[:k]`，所以是 **O(1)**