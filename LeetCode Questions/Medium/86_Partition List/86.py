# submitted at Jun 12, 2024 22:49

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
    # 定義 < x(左邊), > x(右邊) dummy 節點
    left_dummy, right_dummy = ListNode(None), ListNode(None)
    
    # 先定義最後尾，最後會遍歷找下去直到真正的尾
    left_tail, right_tail = left_dummy, right_dummy
    
    while head:
      if head.val < x:
        # 遍歷時數值 < x
        # 將 < x 的節點紀錄至left_dummy(left_tail相當於left_dummy的cur)
        left_tail.next = head
        left_tail = left_tail.next
      else:
        # 遍歷時數值 > x
        # 將 > x 的節點紀錄至right_dummy(right_tail相當於right_dummy的cur)
        right_tail.next = head
        right_tail = right_tail.next
      head = head.next
        
    # 將 < x 最後尾串接 > x 的頭
    left_tail.next = right_dummy.next
    
    # 將 > x 最後尾串接 None
    right_tail.next = None
    
    return left_dummy.next