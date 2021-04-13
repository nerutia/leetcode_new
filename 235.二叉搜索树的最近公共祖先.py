#
# @lc app=leetcode.cn id=235 lang=python3
#
# [235] 二叉搜索树的最近公共祖先
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val < q.val:  # 保证p左q右
            p, q = q, p
        if root.val >= q.val and root.val <= p.val:
            return root
        if root.val > q.val:
            root = root.left
        else:
            root = root.right
        return self.lowestCommonAncestor(root, p, q)
# @lc code=end

