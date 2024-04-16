# submitted at Apr 17, 2024 00:09
class Solution:
  def romanToInt(self, s: str) -> int:
    roman = {
      'I': 1, 'V': 5, 'X': 10,
      'L': 50, 'C': 100, 'D': 500,
      'M': 1000
    }

    num = 0

    for i in range(len(s)):
      if i < len(s) -1 and roman[s[i]] < roman[s[i+1]]:
          # 因為左減不能跨過一位數
          # 例如三位數左邊只能是二位數，三位數左邊不能是一位數。
          # 99不可以用IC表示，而是用XCIX表示(100-10)+(10-1)=99。
          # 且左減數字不能超過1位，譬如8不能寫成IIX，而是VIII
          # 因此每次檢查的時先判斷下一個字母代表的數是否>當下的字母
          # 有的話代表要用減法(後面數字 - 前面數字)
          num -= roman[s[i]]
      else:
        # 其餘則都是加法
        num += roman[s[i]]

    return num
