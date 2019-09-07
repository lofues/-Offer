# -*- coding:utf-8 -*-
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if pHead is None:
            return None
        dummyhead = RandomListNode(pHead.label)
        dummyhead.random = pHead.random
        tail = dummyhead
        while pHead.next is not None:
            pHead = pHead.next

            new_node = RandomListNode(pHead.label)
            new_node.random = pHead.random
            tail.next = new_node
            tail = new_node

        return dummyhead