'''
Author: your name
Date: 2021-04-25 18:38:54
LastEditTime: 2021-04-25 19:37:06
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \tmp\485.最大连续-1-的个数.py
'''
#
# @lc app=leetcode.cn id=485 lang=python3
#
# [485] 最大连续 1 的个数
#

# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        r = 0
        t =  0
        for i in nums:
            if i == 0:
                r = max(r, t)
                t = 0
            else:
                t += 1
        return max(r, t)
# @lc code=end

