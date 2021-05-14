'''
Description: 
Version: 1.0
Author: hqh
Date: 2021-05-11 10:31:13
LastEditors: hqh
LastEditTime: 2021-05-11 10:51:04
'''
#
# @lc app=leetcode.cn id=653 lang=python3
#
# [653] 两数之和 IV - 输入 BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        return self.findTar(root, k, root)

    def findTar(self, root, k, rt):
        if not root:
            return False
        t = k - root.val
        if t != root.val and self.findVal(rt, t):
            return True
        return self.findTar(root.left, k, rt) or self.findTar(root.right, k, rt)

    def findVal(self, rt, v):
        if not rt:
            return False
        if rt.val < v:
            return self.findVal(rt.right, v)
        if rt.val > v:
            return self.findVal(rt.left, v)
        return True

    # 大佬
    # 遍历二叉树+HashSet


# @lc code=end
