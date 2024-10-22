# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

    def dfs(node: Optional[TreeNode], curr_sum: int):
      if not node:
        # node is None
        return False
      
      curr_sum += node.val

      # check if is leaf node
      if not node.left and not node.right:
        # leaf node, check current sum equal targetSum
        return curr_sum == targetSum

      # Not leaf node, keep recursion
      return dfs(node.left, curr_sum) or dfs(node.right, curr_sum)
  
    return dfs(root, 0)