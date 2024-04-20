# submitted at Apr 20, 2024 13:11
class Solution:
  def isSubsequence(self, s: str, t: str) -> bool:
    s_length = len(s)
    a_point = 0
    
    if s_length == 0:
      return True

    for i in range(len(t)):
      if t[i] == s[a_point]:
        a_point += 1
      if a_point >= s_length:
        # 提早結束或剛好t的最後一個字也是s的最後一個字
        return True
    return False