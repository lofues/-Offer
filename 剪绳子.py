# -*- coding:utf-8 -*-
class Solution:
    def cutRope(self, number):
        # write code here
        if number == 2:return 1
        elif number == 3:return 2
        elif number == 4:return 4
        three_times = number // 3
        two_times = number % 3 // 2
        number = number // 3 % 2
        end = number
        return 3 ** three_times * 2 ** two_times * end