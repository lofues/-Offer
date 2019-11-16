# -*- coding:utf-8 -*-
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # write code here
        if not pattern:return not s
        # 匹配当前字符
        first_match = True if s and pattern[0] in (s[0],'.') else False
        if len(pattern) >= 2 and pattern[1] == '*':
            # 匹配当前或者不匹配
            return (first_match and self.match(s[1:],pattern)) or (self.match(s,pattern[2:]))
        else:
            return first_match and self.match(s[1:],pattern[1:])