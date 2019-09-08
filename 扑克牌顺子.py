# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if len(numbers) != 5:
            return False
        numbers.sort()
        count = numbers.count(0)

        if count == 4:
            return True
        else:
            if len(set(numbers[count:])) != 5 - count:
                return False
            tmp = numbers[-1] - numbers[count]
            return tmp <= 4