# -*- coding:utf-8 -*-
import re
class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        regex_int = re.compile('^[+-]?\d+$')
        regex_float = re.compile('^[+-]?\d*\.\d+$')
        regex_e = re.compile('^[+-]?\d*\.?\d*[Ee][+-]?\d+$')
        if re.match(regex_int,s):
            return True
        elif re.match(regex_float,s):
            return True
        elif re.match(regex_e,s):
            return True
        else:
            return False