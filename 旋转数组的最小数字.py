# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        # 使用二分查找
        if len(rotateArray) == 0:
            return None
        elif len(rotateArray) == 1:
            return rotateArray[0]

        left, right = 0, len(rotateArray) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if mid > 0 and rotateArray[mid] < rotateArray[mid - 1]:
                return rotateArray[mid]
            elif rotateArray[mid] > rotateArray[right]:
                left = mid + 1
            else:
                right = mid - 1