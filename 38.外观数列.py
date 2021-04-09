#
# @lc app=leetcode.cn id=38 lang=python3
#
# [38] 外观数列
#

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        def spell(t):
            t = str(t)
            r = []
            c = 0
            m = None
            for i in t:
                if m == None:
                    m = i
                    c = 1
                else:
                    if m == i:
                        c += 1
                    else:
                        r += [str(c), m]
                        m = i
                        c = 1
            r += [str(c), m]
            return ''.join(r)
        if n == 1:
            return '1'
        return spell(self.countAndSay(n-1))
# @lc code=end

