# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if pHead is None:
            return None

        dummyhead = ListNode(None)
        while pHead is not None:
            p = pHead
            pHead = pHead.next
            p.next = dummyhead.next
            dummyhead.next = p
        return dummyhead.next