# submitted at Apr 19, 2024 11:30
class Solution:
  def isPalindrome(self, s: str) -> bool:
    s1 = "".join(c.lower() for c in s if c.isalnum())
    a_point = 0 if len(s1)-1 < 0 else len(s1)-1

    for i, string in enumerate(s1):
      if string != s1[a_point]:
        return False
      a_point -= 1
    return True