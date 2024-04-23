# submitted at Apr 23, 2024 10:53
class Solution:
  def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    # Time complexity: O(mn) => 使用2個不同長度的for迴圈
    # Space complexity: O(n) => 用for迴圈製作hashtable
    hashtable = {}

    for i in magazine:
      if i in hashtable:
        hashtable[i] += 1
      else:
        hashtable[i] = 1
    
    for i in ransomNote:
      if i in hashtable and hashtable[i] != 0: 
        hashtable[i] -= 1
      else:
        # 只要ransomNote有的，而magazine沒有則直接False
        return False
    # ransomNote全部跑完沒有到else => True
    return True