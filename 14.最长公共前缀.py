#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        r = ""
        if strs == []:
            return r
        ml = min([len(i) for i in strs])
        for i in range(ml):
            s = ''
            for j in range(len(strs)):
                if s == '':
                    s = strs[j][i]
                else:
                    if s != strs[j][i]:
                        return r
            r += s
        return r
# @lc code=end

