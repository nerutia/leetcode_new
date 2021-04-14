#
# @lc app=leetcode.cn id=412 lang=python3
#
# [412] Fizz Buzz
#

# @lc code=start
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        r = []
        for v in range(1, n + 1):
            if v % 3 == 0 and v % 5 == 0:
                r.append("FizzBuzz")
            elif v % 3 == 0:
                r.append("Fizz")
            elif v % 5 == 0:
                r.append("Buzz")
            else:
                r.append(str(v))
        return r
# @lc code=end

