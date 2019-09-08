# -*- coding:utf-8 -*-
from itertools import permutations
from functools import reduce
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if len(numbers) == 0:
            return ''
        ret = permutations(numbers)
        ret = [list(x) for x in ret]
        def add(a,b):
               return str(a) + str(b)
        ret = [int(reduce(add,x)) for x in ret]
        return min(ret)