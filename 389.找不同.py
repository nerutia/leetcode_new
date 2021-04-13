#
# @lc app=leetcode.cn id=389 lang=python3
#
# [389] 找不同
#

# @lc code=start
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d = {}
        r = set(t)
        for i in t:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        for i in s:
            d[i] -= 1
            if d[i] == 0:
                r.remove(i)
        return list(r)[0]
        # 大佬
        # 位运算
# @lc code=end

