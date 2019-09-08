# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        # write code here
        if s == '':
            return ''
        ret = s.split(' ')
        ret.reverse()
        return ' '.join(ret)