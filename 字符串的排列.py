# -*- coding:utf-8 -*-
from itertools import permutations


class Solution:
    def Permutation(self, ss):
        # write code here
        if ss == '':
            return []

        return sorted(set(''.join(x) for x in permutations(ss)))