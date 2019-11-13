# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Serialize(self, root):
        # write code here
        if root is None:
            return '#'
        return str(root.val) + ',' + self.Serialize(root.left) + ',' + self.Serialize(root.right)

    def Deserialize(self, s):
        # write code here
        if s == '#':
            return None
        temp = s.split(',')
        return self._deserialize(temp)

    def _deserialize(self, temp):
        if not temp:
            return None
        val = temp.pop(0)
        root = None
        if val != '#':
            root = TreeNode(int(val))
            root.left = self._deserialize(temp)
            root.right = self._deserialize(temp)
        return root