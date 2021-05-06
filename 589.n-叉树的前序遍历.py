'''
Description: 
Version: 1.0
Author: hqh
Date: 2021-05-06 14:17:41
LastEditors: hqh
LastEditTime: 2021-05-06 14:39:10
'''
#
# @lc app=leetcode.cn id=589 lang=python3
#
# [589] N 叉树的前序遍历
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
    # * 迭代
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return
        r = []
        st = [root]
        while st:
            rt = st.pop(0)
            if not rt:
                continue
            r.append(rt.val)
            st = rt.children + st
        return r

    # * 递归
    # def preorder(self, root: 'Node') -> List[int]:
    #     self.res = []

    #     def re(rt):
    #         if rt:
    #             self.res.append(rt.val)
    #             for i in rt.children:
    #                 re(i)

    #     re(root)
    #     return self.res


# @lc code=end
