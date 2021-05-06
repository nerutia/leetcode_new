'''
Description: 
Version: 1.0
Author: hqh
Date: 2021-05-06 00:37:13
LastEditors: hqh
LastEditTime: 2021-05-06 01:46:58
'''
#
# @lc app=leetcode.cn id=530 lang=python3
#
# [530] 二叉搜索树的最小绝对差
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        self.v = 9999999

        # 返回值l, r是以rt为根的二叉树的取值范围
        def re(rt):
            if rt.left:
                l, _ = re(rt.left)
                self.v = min(self.v, rt.val - _)
            else:
                l = rt.val
            if rt.right:
                _, r = re(rt.right)
                self.v = min(self.v, _ - rt.val)
            else:
                r = rt.val
            return l, r

        re(root)
        return self.v


# @lc code=end
