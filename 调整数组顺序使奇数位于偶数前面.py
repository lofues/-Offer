# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here

        odd = []
        even = []
        for i in range(len(array)):
            if array[i] % 2 == 1:
                odd.append(array[i])
            else:
                even.append(array[i])
        return odd + even
