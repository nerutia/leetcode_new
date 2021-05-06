'''
Description: 
Version: 1.0
Author: hqh
Date: 2021-05-02 01:10:41
LastEditors: hqh
LastEditTime: 2021-05-02 01:14:03
'''
#
# @lc app=leetcode.cn id=520 lang=python3
#
# [520] 检测大写字母
#

# @lc code=start
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) == 1:
            return True
        a, b = word[0], word[1:]
        if a == a.upper():
            return b == b.upper() or b == b.lower()
        return b == b.lower()


# @lc code=end
