'''
Description: 
Version: 1.0
Author: hqh
Date: 2021-05-09 01:08:56
LastEditors: hqh
LastEditTime: 2021-05-09 01:58:35
'''
#
# @lc app=leetcode.cn id=605 lang=python3
#
# [605] 种花问题
#

# @lc code=start
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        p = 0
        while p < len(flowerbed):
            if flowerbed[p]:
                p += 2
                continue
            if p == len(flowerbed) - 1:
                return n <= 1
            if flowerbed[p + 1]:
                p += 1
            else:
                n -= 1
                p += 2
        return n <= 0


# @lc code=end
