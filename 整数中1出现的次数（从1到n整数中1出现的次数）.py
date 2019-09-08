# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        if n == 1:
            return 1
        ret = 0
        for i in range(1,n+1):
            ret += str(i).count('1')
        return ret