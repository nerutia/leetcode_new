'''
Description: 
Version: 1.0
Author: hqh
Date: 2021-05-06 13:15:44
LastEditors: hqh
LastEditTime: 2021-05-06 13:20:53
'''
#
# @lc app=leetcode.cn id=543 lang=python3
#
# [543] 二叉树的直径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.res = 0
        if not root:
            return 0

        def re(rt):
            if rt.left:
                l = re(rt.left)
            else:
                l = 0
            if rt.right:
                r = re(rt.right)
            else:
                r = 0
            self.res = max(self.res, l + r + 1)
            return max(l, r) + 1

        re(root)
        return self.res - 1


# @lc code=end
