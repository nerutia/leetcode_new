'''
Description: 
Version: 1.0
Author: hqh
Date: 2021-05-18 10:54:20
LastEditors: hqh
LastEditTime: 2021-05-18 11:36:42
'''
#
# @lc app=leetcode.cn id=811 lang=python3
#
# [811] 子域名访问计数
#

# @lc code=start
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        r = {}
        for i in cpdomains:
            t, s = i.split(" ")
            c = int(t)
            while "." in s:  # 没有.就停
                if s in r:
                    r[s] += c
                else:
                    r[s] = c
                s = s.split(".", 1)[1]
            if s in r:
                r[s] += c
            else:
                r[s] = c
        res = []
        for a, b in r.items():
            res.append(" ".join([str(b), a]))
        return res


# @lc code=end
