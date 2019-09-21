# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index <= 0:
            return 0
        if index == 1:
            return 1
        ugly = [1]
        index_2 = index_3 = index_5 = 0
        for i in range(index-1):
            cur_ugly = min(ugly[index_2]*2,ugly[index_3]*3,ugly[index_5]*5)
            ugly.append(cur_ugly)
            if cur_ugly % 2 == 0:
                index_2 += 1
            if cur_ugly % 3 == 0:
                index_3 += 1
            if cur_ugly % 5 == 0:
                index_5 += 1
        return ugly[-1]