'''
Author: your name
Date: 2021-04-25 18:29:02
LastEditTime: 2021-04-25 18:37:44
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \tmp\482.密钥格式化.py
'''
#
# @lc app=leetcode.cn id=482 lang=python3
#
# [482] 密钥格式化
#

# @lc code=start
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = list(s)
        while '-' in s:
            s.remove('-')
        s = ''.join(s)
        l = len(s)
        rem = l % k
        if rem != 0:
            r = '-' + s[:rem]
        else:
            r = ''
        for i in range(rem, l, k):
            r += '-' + s[i:i+k]
        r = r[1:]
        return r.upper()
# @lc code=end

