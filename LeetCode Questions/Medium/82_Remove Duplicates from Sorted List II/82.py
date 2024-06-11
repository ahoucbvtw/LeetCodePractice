# submitted at Jun 10, 2024 13:54

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
  def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
    # dummy不能=0，因為題目有說node.val有可能會是0
    dummy = ListNode(None, head)
    nonDuplicated = deque()
    deleteVal = None
    a_point, cur = dummy, head
    
    while cur:
      if a_point.val != cur.val:
        # 當前後2節點值不一樣時，將cur.val加入nonDuplicated queue
        # 並且將a_point往前移動到cur位置
        nonDuplicated.append(ListNode(cur.val))
        a_point = cur
      elif nonDuplicated and a_point.val == cur.val and cur.val != deleteVal:
        # 當nonDuplicated有值且當前a_point.val == cur.val
        # 將nonDuplicated最新加入的刪除(因為題目已經排序好，所以重複的會在一起)
        # 但還是需要將已經刪除過的值給紀錄，以防有多個一樣的值導致刪除錯誤
        deleteVal = cur.val
        nonDuplicated.pop()
      cur = cur.next
    
    if len(nonDuplicated) == 0:
      # 如果nonDuplicated queue內沒有值表示原Linked List節點都是重複
      # 因此全部都需要刪除
      return None
    
    # 若nonDuplicated queue不為0，表示有要重新鏈結的不重複節點
    cur = dummy
    for i in range(len(nonDuplicated)):
      cur.next = nonDuplicated.popleft()
      cur = cur.next
    return dummy.next