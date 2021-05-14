'''
Description: 
Version: 1.0
Author: hqh
Date: 2021-05-11 10:19:05
LastEditors: hqh
LastEditTime: 2021-05-11 10:29:22
'''
#
# @lc app=leetcode.cn id=645 lang=python3
#
# [645] 错误的集合
#

# @lc code=start
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        l = len(nums)
        ori = list(range(1, l + 1))
        loss = set(ori) - set(nums)
        loss = list(loss)[0]
        diff = sum(nums) - sum(ori)
        return [diff + loss, loss]


# @lc code=end
