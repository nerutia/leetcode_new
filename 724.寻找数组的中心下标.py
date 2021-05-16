'''
Description: 
Version: 1.0
Author: hqh
Date: 2021-05-16 20:23:34
LastEditors: hqh
LastEditTime: 2021-05-16 20:46:34
'''
#
# @lc app=leetcode.cn id=724 lang=python3
#
# [724] 寻找数组的中心下标
#

# @lc code=start
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return -1
        ls, rs = 0, sum(nums[1:])
        if ls == rs:
            return 0
        for p in range(1, len(nums) - 1):
            ls += nums[p - 1]
            rs -= nums[p]
            if ls == rs:
                return p
        ls, rs = sum(nums[:-1]), 0
        if ls == rs:
            return len(nums) - 1
        return -1


# @lc code=end
