'''
Description: 
Version: 1.0
Author: hqh
Date: 2021-05-15 22:19:12
LastEditors: hqh
LastEditTime: 2021-05-15 22:31:48
'''
#
# @lc app=leetcode.cn id=697 lang=python3
#
# [697] 数组的度
#

# @lc code=start
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        d = {}
        num = {}
        n = 0
        l = 0
        for idx, val in enumerate(nums):
            if val in d:
                num[val] += 1
            else:
                d[val] = idx
                num[val] = 1
            if n < num[val]:
                n = num[val]
                l = idx + 1 - d[val]
            elif n == num[val]:
                l = min(l, idx + 1 - d[val])
        return l


# @lc code=end
