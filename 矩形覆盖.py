# -*- coding:utf-8 -*-
"""
    类似fibonacci数列
"""
class Solution:
    def rectCover(self, number):
        # write code here
        if number <= 0:return 0
        elif number == 1:return 1
        elif number == 2:return 2
        p,q = 1,2
        for i in range(3,number+1):
            p,q = q,p+q
        return q