# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if pRoot is None:
            return []
        q = [(pRoot,1)]
        ret = []
        while q:
            cur_node,level = q.pop(0)
            if cur_node:
                if level > len(ret):
                    ret.append([cur_node.val])
                else:
                    ret[-1].append(cur_node.val)
                if cur_node.left:
                    q.append((cur_node.left,level+1))
                if cur_node.right:
                    q.append((cur_node.right,level+1))
        return ret