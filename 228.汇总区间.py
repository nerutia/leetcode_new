#
# @lc app=leetcode.cn id=228 lang=python3
#
# [228] 汇总区间
#
from typing import List
# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        r = []
        is_st = True
        op, ed = None, None
        for i in nums:
            print('p:', op, ed)
            if is_st:  # 开头
                is_st = False
                op = i
                ed = op
            elif i == ed + 1:  # 不是开头
                ed = i
            else:  # 结尾
                print(op, ed)
                if op == ed:
                    r.append(str(op))
                else:
                    r.append(str(op) + "->" + str(ed))
                op = i
                ed = op
        if op == ed:
            r.append(str(op))
        else:
            r.append(str(op) + "->" + str(ed))
        return r
# @lc code=end
s = Solution()
s.summaryRanges([0,1,2,4,5,7])
