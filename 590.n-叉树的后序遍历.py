'''
Description: 
Version: 1.0
Author: hqh
Date: 2021-05-06 14:32:55
LastEditors: hqh
LastEditTime: 2021-05-06 14:52:26
'''
#
# @lc app=leetcode.cn id=590 lang=python3
#
# [590] N 叉树的后序遍历
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
    # * 递归
    # def postorder(self, root: 'Node') -> List[int]:
    #     self.res = []

    #     def re(rt):
    #         if rt:
    #             for i in rt.children:
    #                 re(i)
    #             self.res.append(rt.val)

    #     re(root)
    #     return self.res

    # 大佬：
    # 迭代的先序遍历稍改一下，改成根右左，遍历后的序列反转过来就是后序
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return
        r = []
        st = [root]
        while st:
            rt = st.pop()
            if not rt:
                continue
            r.append(rt.val)
            st = st + rt.children
        return r[::-1]


# @lc code=end
