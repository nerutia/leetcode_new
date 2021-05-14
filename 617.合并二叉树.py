'''
Description: 
Version: 1.0
Author: hqh
Date: 2021-05-10 00:49:10
LastEditors: hqh
LastEditTime: 2021-05-10 01:21:10
'''
#
# @lc app=leetcode.cn id=617 lang=python3
#
# [617] 合并二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root1:
            return root2
        return self.merge(root1, root2)

    def merge(self, r1, r2):
        if not r2:
            return r1
        if not r1:
            return r2
        r1.val += r2.val
        if r2.left:
            r1.left = self.merge(r1.left, r2.left)
        if r2.right:
            r1.right = self.merge(r1.right, r2.right)
        return r1

        # 大佬
        # if t1 and t2 :
        #     t1.val += t2.val
        #     t1.left = self.mergeTrees(t1.left, t2.left)
        #     t1.right = self.mergeTrees(t1.right, t2.right)
        #     return t1
        # return t1 or t2


# @lc code=end
