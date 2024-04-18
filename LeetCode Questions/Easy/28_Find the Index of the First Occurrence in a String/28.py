# submitted at Apr 18, 2024 10:25
class Solution:
  def strStr(self, haystack: str, needle: str) -> int:
    a_point = len(needle)

    for i in range(len(haystack)-a_point+1):
      if haystack[i:i+a_point] == needle:
        return i
    return -1