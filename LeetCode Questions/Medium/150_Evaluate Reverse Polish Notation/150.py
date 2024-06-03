# submitted at Jun 03, 2024 15:01
class Solution:
  def evalRPN(self, tokens: list[str]) -> int:
    caulate_stack = []
    operators = {'+', '-', '*', '/'}
    for token in tokens:
      if token not in operators:
        # 當不是運算符時(純數字)，轉成數字後加入stack
        caulate_stack.append(int(token))
      else:
        # 若遇到運算符，將stack最後2個數字pop出來進行運算
        # 運算完後再放回stack
        pop1 = caulate_stack.pop()
        pop2 = caulate_stack.pop()
        
        match token:
          case "+":
            caulate_stack.append(pop1 + pop2)
          case "-":
            # 注意減數與被減數是哪個數字
            caulate_stack.append(pop2 - pop1)
          case "*":
            caulate_stack.append(pop1 * pop2)
          case "/":
            # 注意除數與被除數是哪個數字以及最後要取整數
            caulate_stack.append(int(pop2 / pop1))
    return caulate_stack[-1]