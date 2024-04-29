# submitted at Apr 29, 2024 21:55
class Solution:
  def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
      return False
    
    hashTable = {}
    for i in s:
      try:
        hashTable[i] += 1
      except:
        hashTable[i] = 1
    
    for i in t:
      try:
        hashTable[i] -= 1
      except:
        return False
      if hashTable[i] == 0:
        hashTable.pop(i)

    return True if not hashTable else False