# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        # write code here
        if s == '':
            return 0
        flag = True
        if s[0] == '+':
            if len(s) == 1:
                return 0
            s = s[1:]
            flag = True
        elif s[0] == '-':
            if len(s) == 1:
                return 0
            s = s[1:]
            flag = False
        if s[0] == '0':
            return 0

        ret = 0
        i = 0
        for number in s[::-1]:
            if 48 <= ord(number) <= 57:
                ret += 10 ** i * (ord(number) - 48)
                i += 1
            else:
                return 0
        if flag:
            return ret
        else:
            return -ret