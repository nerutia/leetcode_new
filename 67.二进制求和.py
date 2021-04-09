#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def add(sa, sb, c):
            s = int(sa) + int(sb) + int(c)
            return str(s % 2), s // 2
        if len(b) > len(a):
            a, b = b, a
        a, b = list(a[::-1]), list(b[::-1])
        c = 0
        for i in range(len(b)):
            a[i], c = add(a[i], b[i], c)
        for i in range(len(b), len(a)):
            a[i], c = add(a[i], '0', c)
        if c == 1:
            a.append('1')
        return ''.join(a[::-1])
        # 大佬
        # return bin(int(a,2)+int(b,2))[2:]
# @lc code=end

