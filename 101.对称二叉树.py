#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        def re(le, ri):
            if le and ri:
                if le.val != ri.val:
                    return False
                return re(le.left, ri.right) and re(le.right, ri.left)
            if le or ri:
                return False
            return True
        return re(root.left, root.right)
# @lc code=end

