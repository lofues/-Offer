# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        if not array:
            return
        greatest_sum = array[0]
        cur_sum = 0
        for num in array:
            cur_sum += num

            if greatest_sum < cur_sum:
                greatest_sum = cur_sum
            if cur_sum < 0:
                cur_sum = 0
        return greatest_sum