# submitted at Apr 16, 2024 00:27
class Solution:
  def lengthOfLastWord(self, s: str) -> int:
    # 因為只需要計算字串內的最後一個副字串字數是多少
    # 因此先把字串前後的空格刪除，再計算最後的副字串字數
    newString = s.strip()
    
    return len(newString.split(" ")[-1])