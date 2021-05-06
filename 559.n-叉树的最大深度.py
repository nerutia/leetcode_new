'''
Description: 
Version: 1.0
Author: hqh
Date: 2021-05-06 13:28:58
LastEditors: hqh
LastEditTime: 2021-05-06 13:34:01
'''
#
# @lc app=leetcode.cn id=559 lang=python3
#
# [559] N 叉树的最大深度
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0

        def re(rt, r):
            if not rt.children:
                return r
            res = 0
            for i in rt.children:
                res = max(res, re(i, r + 1))
            return res

        return re(root, 1)

        # 大佬
        # if not root:
        #     return 0
        # if not root.children:
        #     return 1
        # return max(self.maxDepth(child)+1 for child in root.children)


# @lc code=end
