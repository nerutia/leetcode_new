'''
Description: 
Version: 1.0
Author: hqh
Date: 2021-05-18 13:28:20
LastEditors: hqh
LastEditTime: 2021-05-18 13:41:12
'''
#
# @lc app=leetcode.cn id=819 lang=python3
#
# [819] 最常见的单词
#

# @lc code=start
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.replace('!', ' ')
        paragraph = paragraph.replace('?', ' ')
        paragraph = paragraph.replace("'", ' ')
        paragraph = paragraph.replace(';', ' ')
        paragraph = paragraph.replace(".", ' ')
        paragraph = paragraph.replace(',', ' ')
        st = paragraph.split(" ")
        d = {}
        r = ""
        c = 0
        for s in st:
            s = s.lower()
            if s == ' ' or s == '' or s in banned:
                continue
            if s in d:
                d[s] += 1
            else:
                d[s] = 1
            if d[s] > c:
                c = d[s]
                r = s
        return r


# @lc code=end
