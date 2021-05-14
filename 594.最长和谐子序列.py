'''
Description: 
Version: 1.0
Author: hqh
Date: 2021-05-08 00:40:33
LastEditors: hqh
LastEditTime: 2021-05-08 01:15:31
'''
#
# @lc app=leetcode.cn id=594 lang=python3
#
# [594] 最长和谐子序列
#

# @lc code=start
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        r = 0
        for i in d.keys():
            if i - 1 in d:
                r = max(r, d[i] + d[i - 1])
            if i + 1 in d:
                r = max(r, d[i] + d[i + 1])
        return r


# @lc code=end
