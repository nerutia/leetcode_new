#
# @lc app=leetcode.cn id=405 lang=python3
#
# [405] 数字转换为十六进制数
#

# @lc code=start
class Solution:
    def toHex(self, num: int) -> str:
        hex="0123456789abcdef"
        res=""
        for _ in range(8):
            res=hex[num&15]+res
            num=num>>4
            if num==0:
                break
        return res
# @lc code=end

