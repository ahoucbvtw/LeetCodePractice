# submitted at Apr 13, 2024 17:34
class Solution:
  # O(log(n))
  def posBinary(self, array: list[int]) -> int:
    '''判斷>0的數字有幾個的2元搜尋法'''
    left_p = 0
    right_p = len(array) - 1
    
    while left_p <= right_p:
      # print('left_p = ', left_p)
      # print('right_p = ', right_p)
      mid = (left_p + right_p) // 2
      # print('mid = ', mid)
      if left_p != right_p:
        # 左右指標不在同個位置
        if array[mid] <= 0:
          # 因為是判斷>0，所以當array[mid]不是>0時
          # 就需要把左指標(陣列最小值的方向)往後移動到mid + 1
          left_p = mid + 1
        elif array[mid] > 0 and (array[mid-1] != 0 and array[mid-1] > 0):
          # (若>0)且(mid左邊的一個數字!=0和>0的話)
          # 表示目前檢測的位置左邊還有比它小的正整數
          # 因此將右指標往前移動到mid - 1
          right_p = mid - 1
        else:
          # 若上述條件都不符合的話
          # 表示已經找到最小>0正整數的index位置
          # 所以使用陣列總數量　-　當下檢查的位置　=　>0的數量
          return len(array) - mid
      else:
        # 左右指標在同個位置表示陣列所有數值已經全部遍歷完畢
        if array[mid] > 0:
          # 若此時>0，表示找到最小>0正整數的index位置
          # 所以使用陣列總數量　-　當下檢查的位置　=　>0的數量
          return len(array) - mid
        else:
          # 因為已經遍歷完畢陣列所有數值
          # 且當下檢查的位置又非>0
          # 表示此陣列並未有任何>0的正整數，因此return 0
          return 0
        # print("="*100)
    # 此為若全正整數
    # 表示右指標會一直減到<左指摽還找不到最小正整數迴圈就停止
    # 即當下檢查的位置就是最小正整數
    # 因此陣列總數量　-　當下檢查的位置　=　>0的數量
    return len(array) - mid

  def negBinary(self, array: list[int]) -> int: 
    '''判斷<0的數字有幾個的2元搜尋法'''
    left_p = 0
    right_p = len(array) - 1
    
    while left_p <= right_p:
      # print('left_p = ', left_p)
      # print('right_p = ', right_p)
      mid = (left_p + right_p) // 2
      # print('mid = ', mid)
      if left_p != right_p:
        # 左右指標不在同個位置
        if array[mid] >= 0:
          # 因為是判斷<0，所以當array[mid]不是>=0時
          # 就需要把右指標(陣列最大值的方向)往前移動到mid - 1
          right_p = mid - 1
        elif array[mid] < 0 and (array[mid+1] != 0 and array[mid+1] < 0):
          # (若<0)且(mid右邊的一個數字!=0和<0的話)
          # 表示目前檢測的位置右邊還有比它大的負整數
          # 因此將右指標往前移動到mid + 1
          left_p = mid + 1
        else:
          # 若上述條件都不符合的話
          # 表示已經找到最大<0負整數的index位置
          # 所以當下檢查的位置+1　=　<0的數量
          return (mid) + 1
      else:
        # 左右指標在同個位置表示陣列所有數值已經全部遍歷完畢
        if array[mid] < 0:
          # 若此時<0，表示找到最大<0負整數的index位置
          # 所以當下檢查的位置+1　=　<0的數量
          return (mid) + 1
        elif array[mid] > 0 and array[mid-1] < 0:
          # 若此時檢查的數值>0且前一個數值<0
          # 表示最大的負整數位置在mid - 1
          # 因此輸出(當下檢查的位置-1)+1 = <0的數量
          return (mid - 1) + 1
        else:
          # 因為已經遍歷完畢陣列所有數值
          # 且當下檢查的位置又非<0
          # 表示此陣列並未有任何<0的負整數，因此return 0
          return 0
        # print("="*100)
    # 此為若右指標<左指標還找不到最大負整數迴圈就停止[0,1]
    # 即完全找不到任何<0的負整數，因此return 0
    return 0
    
  def maximumCount(self, nums: list[int]) -> int:
    '''比較找正整數的2元搜尋法以及找最小正整數的2元搜尋法哪個數量較多'''
    return max(self.posBinary(nums), self.negBinary(nums))