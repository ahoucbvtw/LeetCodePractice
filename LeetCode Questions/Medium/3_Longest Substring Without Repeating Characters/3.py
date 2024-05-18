# submitted at May 17, 2024 21:58
class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
    stringSet = set()
    L = 0
    ans = 0
    
    for R in range(len(s)):
      while s[R] in stringSet:
        stringSet.remove(s[L])
        L += 1
      stringSet.add(s[R])
      ans = max((R-L)+1, ans)
    return ans