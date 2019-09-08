# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.num = []

    def Insert(self, num):
        # write code here
        self.num.append(num)
        self.num.sort()

    def GetMedian(self, data):
        # write code here
        count = len(self.num)
        if self.num == []:
            return None
        elif count % 2 == 1:
            return self.num[count // 2]
        else:
            return (self.num[(count - 1) // 2] + self.num[count // 2]) / 2.0