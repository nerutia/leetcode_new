'''
Description: 
Version: 1.0
Author: hqh
Date: 2021-05-16 22:53:22
LastEditors: hqh
LastEditTime: 2021-05-16 22:55:01
'''
#
# @lc app=leetcode.cn id=771 lang=python3
#
# [771] 宝石与石头
#

# @lc code=start
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        s = set(jewels)
        r = 0
        for i in stones:
            if i in s:
                r += 1
        return r


# @lc code=end
