#
# @lc app=leetcode.cn id=290 lang=python3
#
# [290] 单词规律
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        st = s.split(' ')
        d = {}
        dr = {}
        if len(pattern) != len(st):
            return False
        for i, j in zip(pattern, st):
            if i in d:
                if d[i] != j or j not in dr or dr[j] != i:
                    return False
            elif j in dr:
                return False
            d[i] = j
            dr[j] = i
        return True
# @lc code=end

