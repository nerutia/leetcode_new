'''
Description: 
Version: 1.0
Author: hqh
Date: 2021-05-14 10:02:47
LastEditors: hqh
LastEditTime: 2021-05-14 10:09:28
'''
#
# @lc app=leetcode.cn id=674 lang=python3
#
# [674] 最长连续递增序列
#

# @lc code=start
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        l = len(nums)
        r = 0
        t = 0
        for i in range(l - 1):
            if nums[i] >= nums[i + 1]:
                r = max(r, t)
                t = 0
            else:
                t += 1
        return max(r, t) + 1


# @lc code=end
