# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        if tsum <= 1:
            return []
        ret = []
        for a1 in range(1,tsum//2+1):
            for n in range(2,tsum+2):
                if self.parse_sum(a1,n) == tsum:
                    ret.append([x for x in range(a1,a1+n)])
                elif self.parse_sum(a1,n) > tsum:
                    break
        return ret

    def parse_sum(self,a1,n):
        return int((n**2)/2 + a1 * n - n / 2)