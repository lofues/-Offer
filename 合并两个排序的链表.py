# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if pHead1 is None and pHead2 is None:
            return None
        elif pHead1 is not None and pHead2 is None:
            return pHead1
        elif pHead1 is None and pHead2 is not None:
            return pHead2

        dummyhead = ListNode(None)
        tail = dummyhead
        while pHead1 is not None and pHead2 is not None:
            if pHead1.val < pHead2.val:
                tail.next = pHead1
                tail = tail.next
                pHead1 = pHead1.next
            else:
                tail.next = pHead2
                tail = tail.next
                pHead2 = pHead2.next
        tail.next = pHead1 if pHead2 is None else pHead2
        return dummyhead.next