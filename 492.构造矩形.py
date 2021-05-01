'''
Author: your name
Date: 2021-04-25 19:38:39
LastEditTime: 2021-04-25 19:43:07
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \tmp\492.构造矩形.py
'''
#
# @lc app=leetcode.cn id=492 lang=python3
#
# [492] 构造矩形
#

# @lc code=start
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        t = int(area**0.5)
        for i in range(t, -1, -1):
            if area % i == 0:
                return [area // i, i]
# @lc code=end

