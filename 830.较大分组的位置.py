'''
Description: 
Version: 1.0
Author: hqh
Date: 2021-05-18 18:53:44
LastEditors: hqh
LastEditTime: 2021-05-18 21:32:23
'''
#
# @lc app=leetcode.cn id=830 lang=python3
#
# [830] 较大分组的位置
#

# @lc code=start
class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        r = []
        start, stop = 0, 0
        l = len(s)
        while start < l:
            stop = start + 1
            while stop < l and s[start] == s[stop]:
                stop += 1
            if stop - start >= 3:
                r.append([start, stop - 1])
            start = stop
        return r


# @lc code=end
