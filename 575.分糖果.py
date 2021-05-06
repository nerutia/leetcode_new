'''
Description: 
Version: 1.0
Author: hqh
Date: 2021-05-06 14:04:28
LastEditors: hqh
LastEditTime: 2021-05-06 14:16:09
'''
#
# @lc app=leetcode.cn id=575 lang=python3
#
# [575] 分糖果
#

# @lc code=start
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        return min(len(set(candyType)), len(candyType) // 2)


# @lc code=end
