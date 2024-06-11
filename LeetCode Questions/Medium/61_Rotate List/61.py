# submitted at Jun 11, 2024 17:18

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    # 防止題目給的鏈結串列是空的
    if not head:
      return None

    # 先取得此鏈結串列的長度並紀錄最後一個節點
    length, tail = 1, head

    while tail.next:
      tail = tail.next
      length += 1
    
    # 計算k是否有循環整個鏈結串列(k >= length，取餘數)
    cutCounts = k % length

    # 如果餘數剛好=0，表示剛好經歷一個循環，不需要做變動
    if cutCounts == 0:
      return head
    
    # 尋找因rotate而成為新的頭的節點
    # for迴圈向前移動length-k-1步，會到達新頭節點的前一個點
    # 之所以選擇走到這是因為需要在前一個節點鏈結切斷，而它變成新的尾
    cur = head
    for i in range(length - cutCounts - 1):
      cur = cur.next
    
    newhead = cur.next # 從這個節點切斷當rotate後的頭
    cur.next = None # 將此節點設為rotate後的尾
    tail.next = head # 將原先紀錄的尾(切斷後一長串的尾)鏈結尚未rotate的頭

    return newhead