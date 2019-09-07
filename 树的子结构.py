# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if pRoot1 is None or pRoot2 is None:
            return False

        return self.is_subtree(pRoot1, pRoot2) or self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right,
                                                                                                          pRoot2)

    def is_subtree(self, tree1, tree2):
        if tree2 is None:
            return True

        if tree1 is None or tree1.val != tree2.val:
            return False
        else:
            return self.is_subtree(tree1.left, tree2.left) and self.is_subtree(tree1.right, tree2.right)