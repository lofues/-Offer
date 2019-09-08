# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        if len(numbers) <= 1:
            return False
        tmp = [0] * len(numbers)
        for number in numbers:
            tmp[number] += 1
        for i, number in enumerate(tmp):
            if number > 1:
                duplication[0] = i
                return True
        return False
