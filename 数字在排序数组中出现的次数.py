# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        if data == []:
            return 0
        elif len(data) > 1:
            if k < data[0] or k > data[-1]:
                return 0
        count = 0
        for num in data:
            if num == k:
                count += 1
            elif num > k:
                break
        return count
