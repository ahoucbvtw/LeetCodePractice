# submitted at Apr 26, 2024 17:31

class Solution:
  def wordPattern(self, pattern: str, s: str) -> bool:
    s_array = s.split(" ")
    # pattern利用find找出重複出現的字母的第一次出現位置在哪，沒重複則寫入其在pattern的位置
    # 因為s字串中間有空格，因此利用split改成陣列去判斷相同單詞是在陣列的第一次出現位置，沒重複一樣寫入其在s新陣列的位置
    # 將2者陣列做比較，相同true，不相同false
    return [pattern.find(i) for i in pattern] == [s_array.index(i) for i in s_array]