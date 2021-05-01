#
# @lc app=leetcode.cn id=500 lang=python3
#
# [500] 键盘行
#

# @lc code=start
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        a = set('qwertyuiop')
        b = set('asdfghjkl')
        c = set('zxcvbnm')
        r = []
        for word in words:
            t = set(word.lower())
            if t.issubset(a) or t.issubset(b) or t.issubset(c):
                r.append(word)
        return r
# @lc code=end

