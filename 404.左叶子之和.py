#
# @lc app=leetcode.cn id=404 lang=python3
#
# [404] 左叶子之和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.rt = 0
        def helper(r, is_left):
            if not r:
                return
            if not r.left and not r.right:
                if is_left:
                    self.rt += r.val
                return
            if r.left:
                helper(r.left, True)
            if r.right:
                helper(r.right, False)
        if not root:
            return 0
        helper(root.left, True)
        helper(root.right, False)
        return self.rt
# @lc code=end

