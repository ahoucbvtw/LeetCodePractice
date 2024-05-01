# submitted at Apr 30, 2024 16:50

# Definition for singly-linked list.
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  def hasCycle(self, head: Optional[ListNode]) -> bool:
    fast = head

    while fast and fast.next:
      # 將慢指針向前1步，快指針向前2步
      head = head.next
      fast = fast.next.next
      
      if head == fast:
        return True
    return False