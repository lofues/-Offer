# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        if pRoot is None:
            return True
        else:
            return self.IsSymmetrical(pRoot.left, pRoot.right)

    def IsSymmetrical(self, node1, node2):
        if node1 is None and node2 is None:
            return True
        elif node1 is None or node2 is None:
            return False
        else:
            return (node1.val == node2.val) and self.IsSymmetrical(node1.left, node2.right) and self.IsSymmetrical(
                node1.right, node2.left)