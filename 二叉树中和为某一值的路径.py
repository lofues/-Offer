# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if root is None:
            return []
        stack = [(root,[root.val])]
        ret = []
        while stack:
            cur_node,path = stack.pop()
            if cur_node:
                left,right = cur_node.left,cur_node.right
                if sum(path) == expectNumber and left is None and right is None:
                    ret.append(path)
                else:
                    if right:
                        stack.append((right,path + [right.val]))
                    if left:
                        stack.append((left,path + [left.val]))
        ret.sort(key = lambda x:len(x),reverse = True)
        return ret