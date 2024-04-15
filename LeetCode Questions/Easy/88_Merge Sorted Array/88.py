# submitted at Mar 30, 2024 09:46
class Solution:
  def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    index = m+n-1
    a_index = m - 1
    b_index = n - 1
    while b_index >= 0:
      if a_index >= 0 and nums1[a_index] > nums2[b_index]:
        nums1[index] = nums1[a_index]
        a_index -= 1
      else:
        nums1[index] = nums2[b_index]
        b_index -= 1
      index -= 1