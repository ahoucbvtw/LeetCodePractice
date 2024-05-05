# LeetCode 80 Remove Duplicates from Sorted Array II
Given an integer array nums sorted in **non-decreasing order**, remove some duplicates `in-place` such that each unique element appears **at most twice**. The relative order of the elements should be kept the **same**.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the **first part** of the array `nums`. More formally, if there are `k` elements after removing the duplicates, then the first `k` elements of `nums` should hold the final result. It does not matter what you leave beyond the first `k` elements.

Return `k` after placing the final result in the first `k` slots of `nums`.

Do **not** allocate extra space for another array. You must do this by **modifying the input array** `in-place` with O(1) extra memory.

Custom Judge:

The judge will test your solution with the following code:
```
int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
  assert nums[i] == expectedNums[i];
}
```

If all assertions pass, then your solution will be **accepted**.

Example 1:
```
Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
```

Example 2:
```
Input: nums = [0,0,1,1,1,1,2,3,3]
Output: 7, nums = [0,0,1,1,2,3,3,_,_]
Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
```

Constraints:

- `1 <= nums.length <= 3 * 10^4`
- `-10^4 <= nums[i] <= 10^4`
- nums is sorted in **non-decreasing** order.

## Topic
- Array
- Two Pointers

## My Thinking
此題目與 [**<font color=#FF0000></b>LeetCode 26 Remove Duplicates from Sorted Array</font>**](https://github.com/ahoucbvtw/LeetCodePractice/tree/main/LeetCode%20Questions/Easy/26_Remove%20Duplicates%20from%20Sorted%20Array) 解題方式相同，差別在於這題是要求 `相同值最多存在2個`。

此題一樣使用 `Two Pointers` 快慢指針來進行解題。

解題思路：
1. 初始化: `慢指針位置 = 0; 快指針位置 = 1(會與for迴圈持續前進); 統計相同數量變數 = 1`<br>統計相同數量變數的變數之所以 = 1，是因為它已經計算當前值的次數
2. 用 `for迴圈` 遍歷，當遇到相同值時，`統計變數 + 1`。<br>當遇到不相同值時，表示目前需要統計新的值，因此` 統計變數 = 1`。
3. 不管何時都需要將 `慢指針後一個位置值 = 快指針當前位置值` 以及 `慢指針位置 + 1`，除了`當統計變數 > 2`時才不需要。<br>因為題目要求重複值最多只能有2個。
4. 上述步驟重複直到全部陣列遍歷完成後，`慢指針位置 + 1` 的位置剛好會是已經按照題目排序完成的陣列。<br>至於 `慢指針位置 + 2` 以後數值則不予理會。


### Complexity
Time complexity: O(n)
> 這裡使用 `for迴圈` 慢慢遍歷，慢慢進行陣列值得兌換，直到迴圈結束，因此為**O(n)**

Space complexity: O(1)
> 此題在進行陣列數值提取、賦予值的時候都是使用指定方式 `nums[slow_point]` 、 `nums[fast_point]` 等，因此為**O(1)**