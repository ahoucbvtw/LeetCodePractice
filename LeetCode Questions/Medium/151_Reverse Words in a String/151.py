# submitted at May 09, 2024 10:40
class Solution:
  def reverseWords(self, s: str) -> str:
    output = ""
    
    # 使用空值去分割成陣列
    # 若是 " a good   example  " 會被分割成下面
    # ['a', 'good', 'example']
    s_array = s.split()
    
    for i in range(len(s_array)-1, -1, -1):
      if i == 0:
        # 反轉的最後一個後面不需要加空格
        output += s_array[i]
      else:
        output += s_array[i] + " "
    return output