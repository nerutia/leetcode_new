'''
Description: 
Version: 1.0
Author: hqh
Date: 2021-05-11 10:14:58
LastEditors: hqh
LastEditTime: 2021-05-11 10:18:19
'''
#
# @lc app=leetcode.cn id=643 lang=python3
#
# [643] 子数组最大平均数 I
#

# @lc code=start
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l = len(nums)
        if l < k:
            return
        s = sum(nums[:k])
        r = s
        for i in range(l - k):
            s += nums[i + k] - nums[i]
            r = max(r, s)
        return r / k


# @lc code=end
