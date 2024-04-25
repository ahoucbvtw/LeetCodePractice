# submitted at Apr 25, 2024 22:26
class Solution:
  def isIsomorphic(self, s: str, t: str) -> bool:
    return [s.find(i) for i in s] == [t.find(i) for i in t]