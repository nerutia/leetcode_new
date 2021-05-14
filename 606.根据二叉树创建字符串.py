'''
Description: 
Version: 1.0
Author: hqh
Date: 2021-05-10 00:09:34
LastEditors: hqh
LastEditTime: 2021-05-10 00:36:25
'''
#
# @lc app=leetcode.cn id=606 lang=python3
#
# [606] 根据二叉树创建字符串
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: TreeNode) -> str:
        if root:
            l = self.tree2str(root.left)
            r = self.tree2str(root.right)
            v = str(root.val)
            if l:
                v += '(' + l + ')'
            elif r:
                v += '()'
            if r:
                v += '(' + r + ')'
            return v


# @lc code=end
