'''
Description: 
Version: 1.0
Author: hqh
Date: 2021-05-11 13:30:57
LastEditors: hqh
LastEditTime: 2021-05-11 15:37:37
'''
#
# @lc app=leetcode.cn id=671 lang=python3
#
# [671] 二叉树中第二小的节点
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        # 大佬
        return self.findMin(root, root.val)

    def findMin(self, root, val):
        if not root:
            return -1
        if root.val > val:
            return root.val
        l = self.findMin(root.left, val)
        r = self.findMin(root.right, val)
        if l < 0:
            return r
        if r < 0:
            return l
        return min(l, r)

    # def findSecondMinimumValue(self, root: TreeNode) -> int:
    #     if not root.left:
    #         return -1
    #     lv = root.left.val
    #     rv = root.right.val
    #     # 左边取第二小，右边取第二小
    #     l = self.findSecondMinimumValue(root.left)
    #     r = self.findSecondMinimumValue(root.right)
    #     if l == -1 and r == -1:  # 都没有第二小，则三者间直接比较
    #         if lv == rv:
    #             return -1
    #         else:
    #             return max(lv, rv)
    #     if l == -1:  # 如果左边没有第二小
    #         if lv == rv:
    #             return r
    #         if lv < rv:
    #             return rv
    #         return min(lv, r)
    #     if r == -1:  # 如果右边没有第二小
    #         if lv == rv:
    #             return l
    #         if rv < lv:
    #             return lv
    #         return min(rv, l)
    #     # 两边都有第二小
    #     if lv == rv:  # 如果相等，取lr小者
    #         return min(l, r)
    #     return max(lv, rv)  # 不等则返回lr大者


# @lc code=end
