# submitted at May 11, 2024 14:55
class Solution:
  def convert(self, s: str, numRows: int) -> str:
    output = ""
    if numRows == 1:
      # 只有一排時只需要輸出該字串
      return s

    for row in range(numRows):
      # 不管是在第幾排，都會有共通的相隔間距值要放入
      common_next_count = (numRows - 1) * 2
      for i in range(row, len(s), common_next_count):
        # 根據每一行去開始計算
        # 使用for迴圈＋跳過一個共通的相隔間距值表示一個zigzag循環
        output += s[i]
        if 0 < row < numRows - 1 and (i + ((common_next_count) - (2 * row))) < len(s):
          # 除了頭尾兩排的中間排
          # 在每個zigzag循環時除了共通的外，還需要加一次值
          # 需要加 i + ((common_next_count) - (2 * row)) < len(s) 是因為防止指定位置超過字串長度
          output += s[i + ((common_next_count) - (2 * row))]
    return output