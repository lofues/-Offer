# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.in_stack = []
        self.pop_stack = []

    def push(self, node):
        # write code here
        assert type(node) is int

        while self.pop_stack:
            self.in_stack.append(self.pop_stack.pop())
        self.in_stack.append(node)

    def pop(self):
        # return xx
        while self.in_stack:
            self.pop_stack.append(self.in_stack.pop())

        if len(self.pop_stack) <= 0:
            return None
        else:
            return self.pop_stack.pop()