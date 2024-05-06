# submitted at May 06, 2024 10:23
import random
class RandomizedSet:
  def __init__(self):
    self.element = dict()
    self.array = list()
    self.lastVal_array = int()

  def insert(self, val: int) -> bool:
    if val not in self.element:
      self.array.append(val)
      self.element[val] = len(self.array) - 1
      return True
    else:
      return False

  def remove(self, val: int) -> bool:
    if val in self.element:
    # 要刪除的值和最後一個值對調array, dict
      self.lastVal_array = self.array[-1]
      # 對調
      self.array[self.element[val]], self.array[-1] = self.array[-1], self.array[self.element[val]]
      self.element[val], self.element[self.lastVal_array] = self.element[self.lastVal_array], self.element[val]
      # 刪除
      self.array.pop()
      self.element.pop(val)
      return True
    else:
      return False

  def getRandom(self) -> int:
    return random.choice(self.array)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()