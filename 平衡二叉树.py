# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        if pRoot is None:
            return True
        return abs(self.parse_height(pRoot.left) - self.parse_height(pRoot.right)) <= 1 and self.IsBalanced_Solution(
            pRoot.left) and self.IsBalanced_Solution(pRoot.right)

    def parse_height(self, root):
        if root is None:
            return 0
        return max(self.parse_height(root.left), self.parse_height(root.right)) + 1