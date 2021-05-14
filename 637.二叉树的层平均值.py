'''
Description: 
Version: 1.0
Author: hqh
Date: 2021-05-10 01:23:03
LastEditors: hqh
LastEditTime: 2021-05-10 01:30:44
'''
#
# @lc app=leetcode.cn id=637 lang=python3
#
# [637] 二叉树的层平均值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return []
        r = []
        st = [root]
        st_ = []
        while st:
            t = []
            while st:
                rt = st.pop(0)
                if not rt:
                    continue
                st_.append(rt.left)
                st_.append(rt.right)
                t.append(rt.val)
            if t:
                r.append(sum(t) / len(t))
            st = st_
            st_ = []
        return r
        # 大佬
        # ans, level = [], root and [root]
        # while level:
        #     ans.append(sum(n.val for n in level) / len(level))
        #     level = [k for n in level for k in (n.left, n.right) if k]
        # return ans


# @lc code=end
