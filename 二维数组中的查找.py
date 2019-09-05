# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        if len(array) == 0 or len(array[0]) == 0:
            return False
        for i, v in enumerate(array):
            if target < v[0]:
                break
            elif target > v[-1]:
                continue
            else:
                if self.search(v, 0, len(v) - 1, target):
                    return True
        return False

    def search(self, array, start, end, target):
        if start > end:
            return False
        while start <= end:
            mid = start + (end - start) // 2
            if target == array[mid]:
                return True
            elif target < array[mid]:
                end = mid - 1
            else:
                start = mid + 1
        return False