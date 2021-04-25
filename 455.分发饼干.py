'''
Author: your name
Date: 2021-04-21 15:00:30
LastEditTime: 2021-04-25 16:10:11
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \tmp\455.分发饼干.py
'''
#
# @lc app=leetcode.cn id=455 lang=python3
#
# [455] 分发饼干
#

# @lc code=start
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # x要大于target，每次x找一个最大的target
        child, biscuit = sorted(g)[::-1], sorted(s)[::-1]
        p = 0
        r = 0
        for i in child:
            if len(biscuit) == 0:
                return r
            if biscuit[0] >= i:
                r += 1
                biscuit.pop(0)
        return r
# @lc code=end


