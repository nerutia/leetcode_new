#
# @lc app=leetcode.cn id=401 lang=python3
#
# [401] 二进制手表
#

# @lc code=start
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        r = []
        s = 0
        while s != 0b10000000000:
            if turnedOn == (s&0b1)+(s>>1&0b1)+(s>>2&0b1)+(s>>3&0b1)+(s>>4&0b1)+(s>>5&0b1)+(s>>6&0b1)+(s>>7&0b1)+(s>>8&0b1)+(s>>9&0b1):
                h = s >> 6
                m = s % 64
                if h < 12 and m < 60:
                    r.append(str(h) + ":" + str(m//10) + str(m%10))
            s += 1
        return r
# @lc code=end

