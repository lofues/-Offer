# -*- coding:utf-8 -*-
class Solution:
    # 返回对应char
    def __init__(self):
        self._s = ''
        self.d = {}
    def FirstAppearingOnce(self):
        # write code here
        for i in self._s:
            if self.d[i] == 1:
                return i
        return '#'
    def Insert(self, char):
        # write code here
        self._s += char
        if char in self.d:
            self.d[char] += 1
        else:
            self.d[char] = 1