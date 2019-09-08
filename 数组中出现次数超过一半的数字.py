# -*- coding:utf-8 -*-
from collections import Counter
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if numbers == []:
            return 0

        counter = Counter(numbers)
        most_common = counter.most_common(1)[0]
        if most_common[1] > len(numbers) // 2:
            return most_common[0]
        else:
            return 0