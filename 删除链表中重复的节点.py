# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if pHead is None:
            return None
        stack = []
        while pHead is not None:
            if pHead.val not in stack:
                stack.append(pHead.val)
                pHead = pHead.next
            else:
                while pHead and pHead.val == stack[-1]:
                    pHead = pHead.next
                stack.pop()
        if stack:
            dummyhead = ListNode(None)
            tail = dummyhead
            for val in stack:
                tail.next = ListNode(val)
                tail = tail.next
            return dummyhead.next
        else:
            return None