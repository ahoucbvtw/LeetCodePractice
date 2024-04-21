# submitted at Apr 21, 2024 12:03
class Solution:
  def intToRoman(self, num: int) -> str:
    romanTable = {
      1: 'I', 5: 'V', 10: 'X',
      50: 'L', 100: 'C', 500: 'D',
      1000: 'M'
    }

    string_num = str(num)
    digits = len(string_num)
    roman = ""

    for i in string_num:
      match i:
        case "4":
            if digits < 4:
              x1 = 5*(int("1"+"0"*(digits-1)))
              x2 = int("1"+"0"*(digits-1))
              roman += f'{romanTable[x2]}{romanTable[x1]}'
        case "9":
            if digits < 4:
              x1 = int("1"+"0"*(digits))
              x2 = int("1"+"0"*(digits-1))
              roman += f'{romanTable[x2]}{romanTable[x1]}'
        case "5":
          x1 = 5*int("1"+"0"*(digits-1))
          roman += f'{romanTable[x1]}'
        case i if 5 < int(i) < 9:
          x1 = 5*(int("1"+"0"*(digits-1)))
          x2 = int("1"+"0"*(digits-1))
          roman += f'{romanTable[x1]}{(int(i)-5)*romanTable[x2]}'
        case _:
          x1 = int("1"+"0"*(digits-1))
          roman += f'{int(i)*romanTable[x1]}'
      digits -= 1
    
    return roman