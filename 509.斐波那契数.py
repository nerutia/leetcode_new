'''
Description: 
Version: 1.0
Author: hqh
Date: 2021-05-02 01:07:45
LastEditors: hqh
LastEditTime: 2021-05-02 01:09:50
'''
#
# @lc app=leetcode.cn id=509 lang=python3
#
# [509] 斐波那契数
#

# @lc code=start
class Solution:
    def fib(self, n: int) -> int:
        r = [0, 1]
        for i in range(n):
            r.append(r[i] + r[i + 1])
        return r[n]


# @lc code=end
