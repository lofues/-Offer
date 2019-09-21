# -*- coding:utf-8 -*-
class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        if n <= 0 or m < 0:
            return -1
        num_list = [x for x in range(n)]
        while len(num_list) > 1:
            length = len(num_list)
            num_list.pop((m - 1) % length)

        return num_list[0]

a = Solution()
print(a.LastRemaining_Solution(5,3))