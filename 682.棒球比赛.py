'''
Description: 
Version: 1.0
Author: hqh
Date: 2021-05-14 11:28:12
LastEditors: hqh
LastEditTime: 2021-05-14 11:41:31
'''
#
# @lc app=leetcode.cn id=682 lang=python3
#
# [682] 棒球比赛
#

# @lc code=start
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        r = []
        for i in ops:
            if i == 'C':
                r.pop(-1)
            elif i == 'D':
                r.append(r[-1] * 2)
            elif i == '+':
                r.append(r[-1] + r[-2])
            else:
                r.append(int(i))
        return sum(r)


# @lc code=end
