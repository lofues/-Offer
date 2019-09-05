# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        # write code here
        if number == 1:
            return 1
        ret = [0] * (number + 1)
        for i in range(1, number + 1):
            for j in range(1, i):
                ret[i] += ret[j]
            ret[i] += 1
        return ret[number]

