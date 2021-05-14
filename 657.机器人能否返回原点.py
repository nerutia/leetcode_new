'''
Description: 
Version: 1.0
Author: hqh
Date: 2021-05-11 10:52:59
LastEditors: hqh
LastEditTime: 2021-05-11 10:58:36
'''
#
# @lc app=leetcode.cn id=657 lang=python3
#
# [657] 机器人能否返回原点
#

# @lc code=start
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x, y = 0, 0
        for i in moves:
            if i == 'U':
                x += 1
            if i == 'D':
                x -= 1
            if i == 'R':
                y += 1
            if i == 'L':
                y -= 1
        return x == 0 and y == 0


# @lc code=end
