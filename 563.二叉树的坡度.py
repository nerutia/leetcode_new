'''
Description: 
Version: 1.0
Author: hqh
Date: 2021-05-06 13:39:07
LastEditors: hqh
LastEditTime: 2021-05-06 13:45:44
'''
#
# @lc app=leetcode.cn id=563 lang=python3
#
# [563] 二叉树的坡度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.res = 0

        def re(rt):
            l = re(rt.left) if rt.left else 0
            r = re(rt.right) if rt.right else 0
            self.res += abs(l - r)
            return l + r + rt.val

        re(root)
        return self.res


# @lc code=end
