# -*- coding:utf-8 -*-
from functools import reduce
from itertools import chain
class Solution:
    def multiply(self, A):
        # write code here
        if len(A) <= 1:
            return []
        def mul(a,b):
            return a * b
        B = [0] * len(A)
        for i in range(len(A)):
            B[i] = reduce(mul,chain(A[:i],A[i+1:]))
        return B