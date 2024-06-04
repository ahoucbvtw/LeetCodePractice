# submitted at Jun 04, 2024 15:01

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    # 建立一個空的節點當作入口
    head = ListNode()
    current = head

    # 後續2個鏈結串列比較直接從入口節點的下一個開始添加直到其中一個鏈結串列為空
    while list1 and list2:
      if list1.val < list2.val:
        current.next = list1
        list1 = list1.next
      else:
        current.next = list2
        list2 = list2.next
      current = current.next

    # 上面迴圈會因為其中一個鏈結串列為空而停止
    # 若2個鍊結串列長度不同，則會少加入後面的值
    # 且由於2個鏈結串列值都是經過由小到大排序
    # 因此最後直接將剩下不為空的鏈結串列加入即可
    current.next = list1 if list1 else list2
    return head.next