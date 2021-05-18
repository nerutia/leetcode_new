'''
Description: 
Version: 1.0
Author: hqh
Date: 2021-05-18 13:42:51
LastEditors: hqh
LastEditTime: 2021-05-18 13:55:22
'''
#
# @lc app=leetcode.cn id=821 lang=python3
#
# [821] 字符的最短距离
#

# @lc code=start
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        st = []
        for idx, val in enumerate(s):
            if val == c:
                st.append(idx)
        r = []
        for i in range(len(s)):
            v = [abs(i - j) for j in st]
            r.append(min(v))
        return r
        # 以前的我
        # pos = [i for i,x in enumerate(s) if x == c]
        # r = list(range(len(s)))
        # for i in r:
        #     r[i] = min([abs(j-i) for j in pos])
        # return r


# @lc code=end
