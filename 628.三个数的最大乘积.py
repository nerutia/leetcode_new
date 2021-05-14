'''
Description: 
Version: 1.0
Author: hqh
Date: 2021-05-10 01:21:51
LastEditors: hqh
LastEditTime: 2021-05-11 10:15:12
'''
#
# @lc app=leetcode.cn id=628 lang=python3
#
# [628] 三个数的最大乘积
#
from typing import List

# @lc code=start
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        a = sorted(nums)
        return max(a[0] * a[1] * a[-1], a[-1] * a[-2] * a[-3])


# @lc code=end
