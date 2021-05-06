'''
Description: 
Version: 1.0
Author: hqh
Date: 2021-05-06 13:34:15
LastEditors: hqh
LastEditTime: 2021-05-06 13:38:16
'''
#
# @lc app=leetcode.cn id=561 lang=python3
#
# [561] 数组拆分 I
#

# @lc code=start
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])


# @lc code=end
