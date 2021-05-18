'''
Description: 
Version: 1.0
Author: hqh
Date: 2021-05-18 10:12:30
LastEditors: hqh
LastEditTime: 2021-05-18 10:25:27
'''
#
# @lc app=leetcode.cn id=804 lang=python3
#
# [804] 唯一摩尔斯密码词
#

# @lc code=start
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        d = [
            ".-",
            "-...",
            "-.-.",
            "-..",
            ".",
            "..-.",
            "--.",
            "....",
            "..",
            ".---",
            "-.-",
            ".-..",
            "--",
            "-.",
            "---",
            ".--.",
            "--.-",
            ".-.",
            "...",
            "-",
            "..-",
            "...-",
            ".--",
            "-..-",
            "-.--",
            "--..",
        ]
        r = set()
        for word in words:
            v = [d[ord(i) - ord('a')] for i in word]
            r.add("".join(v))
        return len(r)


# @lc code=end
