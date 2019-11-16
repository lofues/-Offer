# -*- coding:utf-8 -*-
class Solution:
    def movingCount(self, threshold, rows, cols):
        # write code here
        seen = [[0 for _ in range(cols)] for i in range(rows)]
        def helper(threshold,row,col,seen):
            if not (0<= row < rows and 0<=col<cols):return
            if seen[row][col] != 0:return
            if sum(map(int,str(row)+str(col))) <= threshold:
                seen[row][col] = 1
            else:
                seen[row][col] = -1
                return
            helper(threshold,row+1,col,seen)
            helper(threshold,row-1,col,seen)
            helper(threshold,row,col+1,seen)
            helper(threshold,row,col-1,seen)
        helper(threshold,0,0,seen)
        return sum(num for temp in seen for num in temp if num == 1)