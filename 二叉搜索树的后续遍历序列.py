# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence:
            return False
        if len(sequence) == 1:
            return True
        length = len(sequence)
        root = sequence[-1]
        i = 0
        while sequence[i] < root:
            i += 1
        k = i
        for j in range(i,length-1):
            if sequence[j] < root:
                return False
        left_tree = sequence[:k]
        right_tree = sequence[k:length-1]
        leftis,rightis = True,True
        if left_tree:
            leftis = self.VerifySquenceOfBST(left_tree)
        if right_tree:
            rightis = self.VerifySquenceOfBST(right_tree)
        return leftis and rightis