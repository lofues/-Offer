# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if head is None or k <= 0:
            return None
        fast = head
        slow = head
        count = 1
        while count != k and fast is not None:
            fast = fast.next
            count += 1
        if fast is None:
            return None
        while fast is not None and fast.next is not None:
            fast = fast.next
            slow = slow.next
        return slow
