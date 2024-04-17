# submitted at Apr 17, 2024 21:06
class Solution:
  def longestCommonPrefix(self, strs: list[str]) -> str:
    sort = sorted(strs, key = lambda i:len(i))  # 將排序按照文字量
    prefix = {}  # 搜集前綴除了排完序的第一個外出現幾次
    string_len = len(sort[0])  # 排序過後最少文字的字串
    finish = False  # 找到前綴提前結束訊號
    if string_len == 0:
      # strs陣列為空 => 沒有前綴
      return ""
    elif len(strs) == 1:
      # strs陣列只有一組字串 => 前綴 = 自己
      return sort[0]
    else:
      while string_len > 0 and not finish:
        for index in range(1, len(sort)):
          if sort[0][:string_len] not in prefix:
            # 將新比較的前綴加入dict內
            prefix[sort[0][:string_len]] = 0
          if sort[index][:string_len] == sort[0][:string_len]:
            # 有一樣的前綴+1
            prefix[sort[0][:string_len]] += 1
          if prefix[sort[0][:string_len]] == len(strs)-1:
            # 當前綴計算 = 陣列總數量-1 => 提前找到有相同的前綴
            finish = True
        if not finish:
          # 尚未提前結束都要繼續用
          # sort[0]的最大數量慢慢-1, 慢慢找
          string_len -= 1
      
      # 迴圈結束最後判斷
      if string_len > 0:
        # 有找到前綴
        # 找出在dict內中value最大的前綴
        return max(prefix, key=prefix.get)
      else:
        # string_len == 0
        # 沒有找到前綴
        return ''