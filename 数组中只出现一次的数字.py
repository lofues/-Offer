# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        tmp = []
        for num in array:
            if num in tmp:
                tmp.remove(num)
            else:
                tmp.append(num)
        return tmp