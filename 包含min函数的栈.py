# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []
        self.min_val = None
    def push(self, node):
        # write code here
        self.stack.append(node)
        if self.min_val is None or self.min_val > node:
            self.min_val = node
    def pop(self):
        # write code here
        if len(self.stack) == 0:
            return None
        else:
            ret = self.stack.pop()
            if ret == self.min_val:
                if len(self.stack) == 0:
                    self.min_val = None
                else:
                    self.min_val = min(self.stack)
            return ret
    def top(self):
        # write code here
        if len(self.stack) == 0:
            return None
        else:
            return self.stack[-1]
    def min(self):
        # write code here
        if len(self.stack) == 0:
            return None
        else:
            return self.min_val