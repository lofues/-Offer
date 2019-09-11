# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        if pHead1 is None and pHead2 is None:
            return None
        if pHead1 is None or pHead2 is None:
            return None
        cur1,cur2 = pHead1,pHead2
        while cur1:
            while cur2:
                if cur1.val == cur2.val:
                    return cur1
                cur2 = cur2.next
            cur1 = cur1.next
            cur2 = pHead2
        return None