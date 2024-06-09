# submitted at Jun 10, 2024 01:46

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dummy = ListNode(0, head)
    a_point, cur = dummy, dummy
    
    while cur:
      if cur.next and n == 0:
        # a_point需要延遲n步出發，因此當n==0時就可以出發
        # 當cur不為最後節點且n==0時，a_point要移動
        a_point = a_point.next
      else:
        n -= 1
      
      # cur往下移動
      cur = cur.next
        
    # 因為經過延後n步移動，所以就會造成a_point下個節點就是要刪除的點
    # 因此就要將a_point.next設置成a_point.next.next
    a_point.next = a_point.next.next
    
    return dummy.next