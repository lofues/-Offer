# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        if pHead is None:
            return None
        slow = fast = pHead
        ret = [slow]
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow not in ret:
                ret.append(slow)
            else:
                return slow
        return None