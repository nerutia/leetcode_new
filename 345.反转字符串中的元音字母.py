#
# @lc app=leetcode.cn id=345 lang=python3
#
# [345] 反转字符串中的元音字母
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        l, r = 0, len(s) - 1
        st = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        while l < r:
            if s[l] in st and s[r] in st:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            if s[l] not in st:
                l += 1
            if s[r] not in st:
                r -= 1
        return ''.join(s)
# @lc code=end

