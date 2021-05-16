'''
Description: 
Version: 1.0
Author: hqh
Date: 2021-05-15 23:57:22
LastEditors: hqh
LastEditTime: 2021-05-16 20:23:18
'''
#
# @lc app=leetcode.cn id=720 lang=python3
#
# [720] 词典中最长的单词
#

# @lc code=start
class Solution:
    def longestWord(self, words: List[str]) -> str:
        s = set()
        s.add("")
        arr = sorted(words, key=lambda x: (len(x), x))
        r = ""
        for i in arr:
            if i and i[:-1] in s:
                s.add(i)
                if len(i) > len(r):
                    r = i
        return r


# @lc code=end
