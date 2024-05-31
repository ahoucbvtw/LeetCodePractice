# submitted at May 31, 2024 10:24
class MinStack:
  def __init__(self):
    self.minValue = []
    self.stack = []

  def push(self, val: int) -> None:
    self.stack.append(val)
    if self.minValue:
      self.minValue.append(min(self.minValue[-1], val))
    else:
      self.minValue.append(val)

  def pop(self) -> None:
    self.stack.pop()
    self.minValue.pop()

  def top(self) -> int:
    return self.stack[-1]

  def getMin(self) -> int:
    return self.minValue[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()