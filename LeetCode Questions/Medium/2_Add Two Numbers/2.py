# submitted at Jun 05, 2024 23:59

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    output = ListNode()
    cur = output
    carry = 0 # 進位數值
    
    while l1 or l2:
      # 防止2個鏈結串列長度不同，不同時較少的後面節點val要給0
      value1 = l1.val if l1 else 0
      value2 = l2.val if l2 else 0
      
      # new node
      val = carry + value1 + value2
      
      # 防止相加是十位數
      carry = val // 10  # 更新要進位的數值
      val = val % 10  # 取餘數
      
      # 新增計算完成的節點
      cur.next = ListNode(val)
      
      # 將所有鏈結串列移動至下一個
      cur = cur.next
      
      # 防止輸入串列長度不同，較短的不需要往下一步遍歷直接None
      l1 = l1.next if l1 else None
      l2 = l2.next if l2 else None
    
    # 最後防止相加有進位發生，但迴圈已經結束少加
    if carry != 0:
      cur.next = ListNode(carry)
    return output.next