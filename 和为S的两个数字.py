# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        d = {}
        ret = []
        for i,val in enumerate(array):
            d[val] = i
        for val in array:
            tmp = tsum - val
            if tmp in d:
                if d[tmp] != d[val]:
                    l = [val,tmp]
                    ret.append(l)
                else:
                    continue
        if len(ret) == 0:
            return []
        else:
            return sorted(ret,key = lambda x:x[0]*x[1])[0]