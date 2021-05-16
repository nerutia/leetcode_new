'''
Description: 
Version: 1.0
Author: hqh
Date: 2021-05-16 21:59:02
LastEditors: hqh
LastEditTime: 2021-05-16 22:05:57
'''
#
# @lc app=leetcode.cn id=747 lang=python3
#
# [747] 至少是其他数字两倍的最大数
#

# @lc code=start
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        r = max(nums)
        pos = nums.index(r)
        nums.pop(pos)
        if r >= 2 * max(nums):
            return pos
        return -1


# @lc code=end
