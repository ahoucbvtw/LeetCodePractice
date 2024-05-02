# LeetCode 26 Remove Duplicates from Sorted Array

Given an integer array `nums` sorted in non-decreasing order, remove the duplicates **in-place** such that each unique element appears only **once**. The relative order of the elements should be kept the same. Then return *the number of unique elements in* `nums`.

Consider the number of unique elements of `nums` to be `k`, to get accepted, you need to do the following things:

- Change the array `nums` such that the first `k` elements of `nums` contain the unique elements in the order they were present in `nums` initially. The remaining elements of `nums` are not important as well as the size of `nums`.
- Return `k`.

**Custom Judge:**

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
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
```

Example 2:
```
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
```

Constraints:

- `1 <= nums.length <= 3 * 10^4`
- `-100 <= nums[i] <= 100`
- `nums` is sorted in **non-decreasing** order.

## Topic
- Array
- Two Pointers

## My Thinking
這裡使用 `Two Pointers` 的一種: 快慢指針 `Fast-slow Pointers` == 龜兔演算法 `Hare & Tortoise Algorithm`。

在此題， `Fast Pointer` 只需要一直將其index向前 `+1`<br> `Slow Pointer`
則需要等兩個指針值不相同時將 `Slow Pointer` 所在的 `index+1` 替換成現在 `Fast Pointer` 值後將 `Slow Pointer` 所在的index `+1`

而最後 `Slow Pointer` 所在的index 就剛好 = 已經排列好且刪除重複值的陣列最後一個位置，至於該index後面的值就完全不理會即可，因為不重要。

### Complexity
Time complexity: O(n)
> 因為使用 `for迴圈` 方法從頭開始遍歷，因此為 **O(n)**

Space complexity: O(1)
> 此題從頭到尾都是使用陣列指定方式: `nums[a_index]` 及 `nums[b_index]` 去比對值是否相同，因此為 **O(1)**