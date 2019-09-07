# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if root is None or self.is_leaf(root):
            return root
        root.left, root.right = self.Mirror(root.right), self.Mirror(root.left)
        return root

    def is_leaf(self, root):
        return root.left is None and root.right is None