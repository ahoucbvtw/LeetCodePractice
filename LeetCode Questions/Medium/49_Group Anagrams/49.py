# submitted at May 25, 2024 00:04
class Solution:
  def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
    anagramTable = defaultdict(list)
    
    for string in strs:
      # 計算該字串內各英文字母有多少個
      count_list = [0] * 26  # a ~ z
      for i in string:
        # 將英文字母放進相對應的陣列位置
        # 將文字轉成asci，然後再用該asci值 - a的asci值
        count_list[ord(i) - ord("a")] += 1
      # 將count_list轉字串當key放進table
      anagramTable[tuple(count_list)].append(string)
    return anagramTable.values()