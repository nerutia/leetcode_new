'''
Description: 
Version: 1.0
Author: hqh
Date: 2021-05-16 22:06:07
LastEditors: hqh
LastEditTime: 2021-05-16 22:28:39
'''
#
# @lc app=leetcode.cn id=748 lang=python3
#
# [748] 最短补全词
#

# @lc code=start
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        licensePlate = licensePlate.lower()
        d = {}
        for i in licensePlate:
            if i >= 'a' and i <= 'z':
                if i in d:
                    d[i] += 1
                else:
                    d[i] = 1
        r = ''
        for word in words:
            for i in d:
                v = word.count(i)
                if d[i] > v:
                    break
            else:
                if r == '':
                    r = word
                elif len(word) < len(r):
                    r = word
        return r


# @lc code=end
