# LeetCode 49 Group Anagrams
Given an array of strings `strs`, group **the anagrams** together. You can return the answer in **any order**.

An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
```
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
```

Example 2:
```
Input: strs = [""]
Output: [[""]]
```

Example 3:
```
Input: strs = ["a"]
Output: [["a"]]
```

Constraints:

- `1 <= strs.length <= 10^4`
- `0 <= strs[i].length <= 100`
- `strs[i]` consists of lowercase English letters.

## Topic
- Array
- String
- Sorting
- Hash Table

## My Thinking
此題目有2種解題思路：
1. 將輸入的 `Input` 內的每一個字串做 `sort`，並將遇到相同排序的字串紀錄在 `HashTable` 內<br>使用經過排序的字串當作 `key`，`Input` 內符合的字串當作 `value`，最後 `HashTable.values()` 就是符合題目要求擁有相同字母放在一起。
2. 將 `Input` 內的每一個字串找出來後，先統計字串內的字母數量，再將統計的資訊當作 `key`，並將符合的字串當作 `value` 放進 `HashTable` 內，最後 `HashTable.values()` 就是符合題目要求擁有相同字母放在一起。

而最後我採用 **NeetCode** 的 `方法2`。

因為 `方法1` 會需要對字串做 `sort`，然後又因為字串是放在 `Input Array` 內，因此 `Time complexit = O(m * nlogn)`。

但是 `方法2` 則不需要進行排序，只需要針對陣列中每一個字串的字母數量做統計，因此 `Time complexit = O(mn)`。

而 `O(mn)` 肯定會比 `O(m*nlogn)` 還有優秀，畢竟 `O(m*nlogn)` 他後面還要多乘上一個 `logn`，時間上相對沒有乘肯定來得多。

> 參考影片: **By NeetCode**
>
> `Time complexity = O(mn), Space complexity = O(n)`
> 
> [![Group Anagrams - Categorize Strings by Count - Leetcode 49](https://img.youtube.com/vi/vzdNOK2oB2E/hqdefault.jpg)](https://www.youtube.com/watch?v=vzdNOK2oB2E)


### Complexity
Time complexity: O(mn)
> 因為需要遍歷統計陣列中所有字串的字母數量，因此為 **O(mn)**

Space complexity: O(n)
> 因為使用 `HashTable` 針對相同排序字串或相同字母數量做額外的空間，因此為 **O(n)**。