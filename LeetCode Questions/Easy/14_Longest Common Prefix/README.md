# LeetCode 14 Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string `""`.

Example 1:

```
Input: strs = ["flower","flow","flight"]
Output: "fl"
```

Example 2:

```
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
```

Constraints:

- `1 <= strs.length <= 200`
- `0 <= strs[i].length <= 200`
- `strs[i]` consists of only lowercase English letters.

## Topic
- String
- Trie

## My Thinking
1. 使用排序將陣列內的字串按照**字串數量從小到大排列**
2. 建立當下判斷前綴在陣列中有多少個符合的dict<br>**(排除第一個，因為第一個是我用來比對後面是否有一樣前綴)**
3. 用2個迴圈<br>外面是`最小字串數量=0`及`提前找到前綴`為止<br>裡面是`遍歷除了陣列第一個字串以外`的迴圈
4. 尋找前綴時從`最小數量字串`的全部開始，慢慢從後面刪除一個字母，直到全部遍歷結束<br> ```ex: 第一次：abcd, 第二次：abc, 第三次：ab...```
5. 若每當裡面迴圈遍歷完，`前綴數量 == len(陣列) - 1`，表示提前找到有共同前綴，因此直接跳出所有迴圈
6. 計算dict內出現最多次數的前綴文字

### Good Solution

> From abdullayev_akbar
>
> ```
> class Solution:
>     def longestCommonPrefix(self, v: List[str]) -> str:
>       ans=""
>       v=sorted(v)
>       first=v[0]
>       last=v[-1]
>       for i in range(min(len(first),len(last))):
>           if(first[i]!=last[i]):
>               return ans
>          ans+=first[i]
>       return ans 
> ```

此解題技巧為針對陣列中每一個字串進行比對

先從所有字串第一個字母開始<br>若全部都相同，再增加至字串第二個字母比對，直到有其中一個字串的n個字母與其他不一樣時就輸出ans