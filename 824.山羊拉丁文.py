'''
Description: 
Version: 1.0
Author: hqh
Date: 2021-05-18 13:55:36
LastEditors: hqh
LastEditTime: 2021-05-18 18:57:18
'''
#
# @lc app=leetcode.cn id=824 lang=python3
#
# [824] 山羊拉丁文
#

# @lc code=start
class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        st = sentence.split(" ")
        r = []
        p = 0
        for s in st:
            p += 1
            if s[0] not in 'aeiouAEIOU':
                s = s[1:] + s[0]
            r.append(s + 'ma' + 'a' * p)
        return " ".join(r)


# @lc code=end
