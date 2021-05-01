'''
Author: your name
Date: 2021-04-25 20:20:04
LastEditTime: 2021-04-25 20:55:26
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \tmp\501.二叉搜索树中的众数.py
'''
#
# @lc app=leetcode.cn id=501 lang=python3
#
# [501] 二叉搜索树中的众数
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        r = []
        def re(root):
            if root:
                r.append(root.val)
                re(root.left)
                re(root.right)
        re(root)
        d = {}
        for i in r:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        r = []
        c = 0
        for i in d:
            if d[i] > c:
                c = d[i]
                r = [i]
            elif d[i] == c:
                r.append(i)
        return r
        # 使用中序会产生有序数组
# @lc code=end

