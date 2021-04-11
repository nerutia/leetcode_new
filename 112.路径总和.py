#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if root == None:
            return False
        def match(r, s):
            if r == None:
                return s == targetSum
            s += r.val
            if r.left == None:
                return match(r.right, s)
            if r.right == None:
                return match(r.left, s)
            return match(r.left, s) or match(r.right, s)
        return match(root, 0)
# @lc code=end

