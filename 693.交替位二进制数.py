'''
Description: 
Version: 1.0
Author: hqh
Date: 2021-05-15 21:50:42
LastEditors: hqh
LastEditTime: 2021-05-15 21:54:44
'''
#
# @lc app=leetcode.cn id=693 lang=python3
#
# [693] 交替位二进制数
#

# @lc code=start
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        r = -1
        while n:
            t = n & 1
            if r == -1:
                r = t
            elif r == t:
                return False
            else:
                r = t
            n >>= 1
        return True
        # 大佬
        # int temp=n^(n>>1); return (temp&(temp+1))==0;
        # 因为temp=n^(n>>1)必定满足temp=2^N-1。


# @lc code=end
