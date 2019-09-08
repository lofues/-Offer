# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        if pRoot is None:
            return None
        ans = self.in_order(pRoot)
        if len(ans) < k:
            return None
        elif k < 1:
            return None
        return ans[k - 1]

    def in_order(self, root):
        if root is None:
            return []
        ret = []
        ret.extend(self.in_order(root.left))
        ret.append(root)
        ret.extend(self.in_order(root.right))
        return ret