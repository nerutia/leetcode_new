#
# @lc app=leetcode.cn id=205 lang=python3
#
# [205] 同构字符串
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d, p = {}, {}
        for i, j in zip(s, t):
            if i in d:
                if d[i] == j:
                    continue
                return False
            if j in p:
                return False
            d[i],  p[j] = j, i
        return True
# @lc code=end

