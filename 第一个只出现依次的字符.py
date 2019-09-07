# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if s == '':
            return -1
        d = {}
        for idx, string in enumerate(s):
            if string in d:
                d[string][0] += 1
            else:
                d[string] = [1, idx]
        ret = sorted(sorted(d.items(), key=lambda x: x[1][1]), key=lambda x: x[1][0])
        if ret[0][1][0] == 1:
            return ret[0][1][1]
        else:
            return -1