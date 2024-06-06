# submitted at Jun 06, 2024 21:44

"""
# Definition for a Node.
class Node:
  def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
    self.val = int(x)
    self.next = next
    self.random = random
"""

class Solution:
  def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
    # 需要預設一個 None的key/value
    # 因為題目有可能會指定到 None
    outputTable = { None: None }
    
    # 第一次遍歷全部節點，並將每個節點copy放進Table
    cur = head
    while cur:
      newNode = Node(cur.val)
      outputTable[cur] = newNode # {舊node: copy node(只有val)}
      
      # 移動cur到下一步
      cur = cur.next
    
    # 第二次遍歷將copy的節點所有內容補齊
    cur = head # 讓cur重新回到開頭
    while cur:
      newNode = outputTable[cur]
      # 因為cur.next和cur.random都是node
      # 且這兩個copy節點早就於上一個迴圈被遍歷放進table內
      # 所以直接使用hashtable[node]尋找該copy的節點
      newNode.next = outputTable[cur.next]
      newNode.random = outputTable[cur.random]
      
      # 移動cur到下一步
      cur = cur.next
    
    # 因為只需要return copy的頭
    # 因此直接將舊的頭當作key去搜尋copy節點的頭
    return outputTable[head]