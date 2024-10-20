# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
  def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
    # Time = O(n)
    # Space = O(n)
    queue = deque()
    queue.append(root)
    result = []

    while queue:
      avg = 0
      childnum = len(queue)

      # 這裡不影響時間複雜度
      # 因為不加for只是一個一個拿
      # 但是加了以後只是加快獲取該level的子節點以及填入新的子子節點
      for _ in range(childnum):
        node = queue.popleft()
        avg += node.val
        
        if node.left:
          queue.append(node.left)
        if node.right:
          queue.append(node.right)

      result.append(avg / childnum)
    return result