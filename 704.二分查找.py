'''
Description: 
Version: 1.0
Author: hqh
Date: 2021-05-15 23:04:22
LastEditors: hqh
LastEditTime: 2021-05-15 23:12:29
'''
#
# @lc app=leetcode.cn id=704 lang=python3
#
# [704] 二分查找
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            if nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return -1


# @lc code=end
