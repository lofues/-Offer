# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        ret = s.split(' ')
        return '%20'.join(ret)
        #return s.replace(' ','%20')