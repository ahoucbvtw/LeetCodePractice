# submitted at May 29, 2024 10:45
class Solution:
  def isValid(self, s: str) -> bool:
    stack = []
    for i in s:
        if i == "(" or i == "[" or i == "{":
          stack.append(i)
        elif len(stack) == 0 and (i == ")" or i == "]" or i == "}"):
          # stack內不能先遇到closing bracket
          return False
        else:
          # 成功配對
          match i:
            case i if i == ")" and stack[-1] == "(":
              stack.pop()
            case i if i == "]" and stack[-1] == "[":
              stack.pop()
            case i if i == "}" and stack[-1] == "{":
              stack.pop()
            case _:
              # 沒有配對
              return False
    return stack == []