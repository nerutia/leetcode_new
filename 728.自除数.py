'''
Description: 
Version: 1.0
Author: hqh
Date: 2021-05-16 20:48:55
LastEditors: hqh
LastEditTime: 2021-05-16 21:04:25
'''
#
# @lc app=leetcode.cn id=728 lang=python3
#
# [728] 自除数
#

# @lc code=start
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        r = []
        for i in range(left, right + 1):
            v = i
            while v:
                _t = v % 10
                if _t == 0 or i % _t != 0:
                    break
                v //= 10
            else:
                r.append(i)
        return r


# @lc code=end
