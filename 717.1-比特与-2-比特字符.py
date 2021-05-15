'''
Description: 
Version: 1.0
Author: hqh
Date: 2021-05-15 23:32:17
LastEditors: hqh
LastEditTime: 2021-05-15 23:56:31
'''
#
# @lc app=leetcode.cn id=717 lang=python3
#
# [717] 1比特与2比特字符
#

# @lc code=start
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        if bits[-1] == 1:
            return False
        r = 0
        p = len(bits) - 2
        while p >= 0 and bits[p] == 1:
            r += 1
            p -= 1
        return r % 2 == 0


# @lc code=end
