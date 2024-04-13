# LeetCode 2529 Maximum Count of Positive Integer and Negative Integer

Given an array `nums` sorted in **non-decreasing** order, return the *maximum between the number of positive integers and the number of negative integers*.

- In other words, if the number of positive integers in `nums` is `pos` and the number of negative integers is `neg`, then return the maximum of `pos` and `neg`.

**Note** that `0` is neither positive nor negative.


Example 1:

```
Input: nums = [-2,-1,-1,1,2,3]
Output: 3
Explanation: There are 3 positive integers and 3 negative integers. The maximum count among them is 3.
```

Example 2:

```
Input: nums = [-3,-2,-1,0,0,1,2]
Output: 3
Explanation: There are 2 positive integers and 3 negative integers. The maximum count among them is 3.
```

Example 3:

```
Input: nums = [5,20,66,1314]
Output: 4
Explanation: There are 4 positive integers and 0 negative integers. The maximum count among them is 4.
```

Constraints:

- `1 <= nums.length <= 2000`
- `-2000 <= nums[i] <= 2000`
- `nums` is sorted in a **non-decreasing** order.

**Follow up**: Can you solve the problem in `O(log(n))` time complexity?

## Topic
- Array
- Binary Search
- Counting

## My Thinking
目前想到2種解法<br>
- `2569_1.py` : `O(n)` 遍歷給定的陣列，並直接計算 `pos` and `neg` 個數，最後再找出最大值
- `2569_2.py` 使用題目所說使用 `O(log(n))` 時間複雜度去撰寫<br>而最常見例子是使用2分搜尋法<br>但目前我還想不到該如何只使用一次2分搜尋法，因此先暫時使用多個2分搜尋法來求解<br><br>另外由於才剛練習寫題目，因此寫得有些亂，希望未來多多練習後能夠精簡寫法，讓解題思路更易懂

`ps. 若後續有想到只用一個2分搜尋法會再更新`