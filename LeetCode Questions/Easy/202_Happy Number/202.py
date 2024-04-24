# submitted at Apr 24, 2024 22:46
class Solution:
  def isHappy(self, n: int) -> bool:
    squareTable = {
        "0": "0", "1": "1", "2": "4",
        "3": "9", "4": "16", "5": "25",
        "6": "36", "7": "49", "8": "64",
        "9": "81"
    }
    
    repeatTable = {}
    x = n
    while x != 1:
      if len(str(x)) > 1:
        z = 0
        for i in str(x):
          z += int(squareTable[i])
        x = z
        if x in repeatTable:
          return False
        else:
          repeatTable[x] = 0
      else:
        x = x ** 2
    return True