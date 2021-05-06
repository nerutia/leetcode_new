'''
Description: 
Version: 1.0
Author: hqh
Date: 2021-05-06 13:49:34
LastEditors: hqh
LastEditTime: 2021-05-06 14:03:30
'''
#
# @lc app=leetcode.cn id=572 lang=python3
#
# [572] 另一个树的子树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if not root:
            return not subRoot
        if self.isSame(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSame(self, r1, r2):
        if not r1 and not r2:
            return True
        if r1 and r2 and r1.val == r2.val:
            return self.isSame(r1.left, r2.left) and self.isSame(r1.right, r2.right)
        return False

        # 大佬
        # return str(t) in str(s)


# @lc code=end
