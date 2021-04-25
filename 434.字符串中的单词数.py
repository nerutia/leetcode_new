#
# @lc app=leetcode.cn id=434 lang=python3
#
# [434] 字符串中的单词数
#

# @lc code=start
class Solution:
    def countSegments(self, s: str) -> int:
        s = s.strip(' ')
        if len(s) == 0:
            return 0
        r = 1
        for i in range(len(s) - 1):
            if s[i] != ' ' and s[i + 1] == ' ':
                r += 1
        return r
        # 大佬
        # return len(s.split())
# @lc code=end

