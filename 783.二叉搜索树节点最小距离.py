'''
Description: 
Version: 1.0
Author: hqh
Date: 2021-05-16 22:55:22
LastEditors: hqh
LastEditTime: 2021-05-16 23:23:17
'''
#
# @lc app=leetcode.cn id=783 lang=python3
#
# [783] 二叉搜索树节点最小距离
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        self.pre = None
        self.r = 100000
        self.re(root)
        return self.r

    def re(self, root):
        if root:
            self.re(root.left)
            if self.pre:
                self.r = min(self.r, root.val - self.pre)
            self.pre = root.val
            self.re(root.right)


# @lc code=end
