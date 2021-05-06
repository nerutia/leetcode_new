'''
Description: 
Version: 1.0
Author: hqh
Date: 2021-05-02 00:56:21
LastEditors: hqh
LastEditTime: 2021-05-02 01:07:13
'''
#
# @lc app=leetcode.cn id=507 lang=python3
#
# [507] 完美数
#

# @lc code=start
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
        t = int(num ** 0.5) + 1
        r = 1
        for i in range(2, t):
            if num % i == 0:
                r += i
                v = num // i
                if v > i:
                    r += num // i
        return r == num


# @lc code=end
