#
# @lc app=leetcode.cn id=392 lang=python3
#
# [392] 判断子序列
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        def makeIdx(t):
            d = {}
            for i in range(len(t)):
                v = t[i]
                if v not in d:
                    d[v] = i + 1
            return d
        # 为t建数据库r
        r = []
        for i in range(len(t)):
            r.append(makeIdx(t[i:]))
        # 之后任何s用以下代码查数据库即可
        p = 0
        for i in s:
            if p >= len(r) or i not in r[p]:
                return False
            p += r[p][i]
        return True
        # 大佬
        # 用动态规划记录
# @lc code=end

