'''
Description: 
Version: 1.0
Author: hqh
Date: 2021-05-16 21:44:11
LastEditors: hqh
LastEditTime: 2021-05-16 21:55:47
'''
#
# @lc app=leetcode.cn id=746 lang=python3
#
# [746] 使用最小花费爬楼梯
#

# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        r = []  # r[i]表示走到第i个台阶的最少花费
        for i in cost:
            if len(r) < 2:
                r.append(i)
                continue
            r.append(min(r[-1], r[-2]) + i)
        return min(r[-1], r[-2])


# @lc code=end
