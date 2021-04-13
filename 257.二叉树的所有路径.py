#
# @lc app=leetcode.cn id=257 lang=python3
#
# [257] 二叉树的所有路径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        def re(rt, s):
            if rt.left == None and rt.right == None:
                return r.append(s+"->"+str(rt.val))
            if rt.left:
                re(rt.left, s+"->"+str(rt.val))
            if rt.right:
                re(rt.right, s+"->"+str(rt.val))
        r = []
        if not root:
            return r
        re(root, "")
        return [i[2:] for i in r]
# @lc code=end

