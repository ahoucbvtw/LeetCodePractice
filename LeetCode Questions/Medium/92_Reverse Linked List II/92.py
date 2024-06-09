# submitted at Jun 09, 2024 07:54

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    if right == left:
      # 兩者一樣不需要做更動
      return head
    
    dummy = ListNode(0, head)
    Lpre, cur = dummy, head
    
    # 先找第一個要交換的left點(cur抵達該點就好)
    for i in range(left - 1):
      Lpre, cur = cur, cur.next
    # 找尋下一個交換點right前
    # 先把下一個交換點的前的位置(pre)指定為None
    pre = None
    
    # 在尚未斷開原先連結，先紀錄cur.next值
    # 將cur.next設置為pre(將cur.next往前指定，因為題目說指定位置的區間內要進行反轉)
    # 最後再將Rpe和cur向前移動，不過cur.next已經與原先不一樣
    # 因此只有他是指定剛剛紀錄的值
    for i in range(right - left + 1):
      nextnode = cur.next
      cur.next = pre
      pre, cur = cur, nextnode
    
    # 將left和right節點位置交換並前後都要串起來
    # left點移動到right點
    Lpre.next.next = cur
    
    # right點移動到left點(Lpre.next = right)
    # 因為right點的下一個點已經進行反轉，所以只需要將它的新前節點鏈結即可
    Lpre.next = pre
    
    return dummy.next