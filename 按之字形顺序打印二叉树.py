# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Print(self, pRoot):
        # write code here
        if pRoot is None:
            return []
        q = [(pRoot,1)]
        ret = []
        while q:
            cur_node,level = q.pop(0)
            if cur_node:
                if len(ret) < level:
                    ret.append([cur_node.val])
                else:
                    ret[-1].append(cur_node.val)
                if cur_node.left:
                    q.append((cur_node.left,level+1))
                if cur_node.right:
                    q.append((cur_node.right,level+1))
        for i in range(len(ret)):
            if i % 2 == 1:
                ret[i].reverse()
        return ret